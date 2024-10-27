package main

import (
	"encoding/xml"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Element struct {
	XMLName xml.Name
	Attrs   []xml.Attr `xml:",any,attr"`
	Content []byte     `xml:",chardata"`
	Nodes   []Element  `xml:",any"`
}

var constants = make(map[string]float64)
var stringConstants = make(map[string]string)

func parseElement(e Element, indent string) string {
	result := ""

	switch e.XMLName.Local {
	case "comment":
		return indent + ":: " + strings.TrimSpace(string(e.Content)) + "\n"
	case "array":
		result += indent + parseArray(e) + "\n"
	case "constant":
		result += indent + parseConstant(e) + "\n"
	case "string":
		result += indent + parseStringConstant(e) + "\n"
	case "expression":
		expression := parseExpression(e)
		_, evalResult := evaluateExpression(e)
		result += indent + expression + " => " + evalResult + "\n"
	case "let":
		result += indent + parseLet(e) + "\n"
	default:
		if len(e.Nodes) == 0 {
			result += indent + e.XMLName.Local + " = " + parseValue(string(e.Content)) + ";\n"
		} else {
			result += indent + e.XMLName.Local + " {\n"
			for _, node := range e.Nodes {
				result += parseElement(node, indent+"  ")
			}
			result += indent + "}\n"
		}
	}
	return result
}

func parseArray(e Element) string {
	values := []string{}
	for _, node := range e.Nodes {
		values = append(values, strings.TrimSpace(string(node.Content)))
	}
	return "({ " + strings.Join(values, ", ") + " })"
}

func parseConstant(e Element) string {
	name := ""
	value := ""
	for _, attr := range e.Attrs {
		if attr.Name.Local == "name" {
			name = attr.Value
		}
	}
	value = parseValue(string(e.Content))
	constantValue, _ := strconv.ParseFloat(value, 64)
	constants[name] = constantValue
	return "let " + name + " = " + value + ";"
}

func parseStringConstant(e Element) string {
	name := ""
	value := ""
	for _, attr := range e.Attrs {
		if attr.Name.Local == "name" {
			name = attr.Value
		}
	}
	value = "q(" + parseValue(string(e.Content)) + ")"
	stringConstants[name] = value
	return "let " + name + " = " + value + ";"
}

func parseLet(e Element) string {
	name := ""
	value := ""
	for _, attr := range e.Attrs {
		if attr.Name.Local == "name" {
			name = attr.Value
		}
	}
	value = parseValue(string(e.Content))
	return "let " + name + " = " + value + ";"
}

func parseExpression(e Element) string {
	operator := ""
	operands := []string{}
	for _, node := range e.Nodes {
		if node.XMLName.Local == "operator" {
			operator = strings.TrimSpace(string(node.Content))
		} else {
			operands = append(operands, strings.TrimSpace(string(node.Content)))
		}
	}
	return "?( " + operator + " " + strings.Join(operands, " ") + " )"
}

func evaluateExpression(e Element) (bool, string) {
	switch e.XMLName.Local {
	case "expression":
		operator := ""
		operands := []string{}

		for _, node := range e.Nodes {
			if node.XMLName.Local == "operator" {
				operator = string(node.Content)
			} else if node.XMLName.Local == "operand" {
				operands = append(operands, strings.TrimSpace(string(node.Content)))
			}
		}

		switch operator {
		case "+":
			var total float64
			for _, op := range operands {
				if val, err := strconv.ParseFloat(op, 64); err == nil {
					total += val
				} else if constant, exists := constants[op]; exists {
					total += constant
				} else {
					return false, "Неподдерживаемая операция"
				}
			}
			return true, fmt.Sprintf("%.2f", total)
		case "print":
			if len(operands) > 0 {
				name := operands[0]
				if value, exists := constants[name]; exists {
					return true, fmt.Sprintf("%.2f", value)
				} else if strValue, exists := stringConstants[name]; exists {
					return true, strValue
				}
				return false, "Неподдерживаемая операция"
			}
		}
	}

	return false, "Неподдерживаемая операция"
}

func parseValue(val string) string {
	return strings.TrimSpace(val)
}

func main() {
	decoder := xml.NewDecoder(os.Stdin)
	var root Element

	err := decoder.Decode(&root)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Ошибка при чтении XML: %v\n", err)
		os.Exit(1)
	}

	result := parseElement(root, "")
	fmt.Print(result)
}
