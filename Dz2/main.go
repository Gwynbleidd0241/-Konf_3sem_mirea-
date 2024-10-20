package main

import (
	"encoding/xml"
	"flag"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

type Config struct {
	VisualizationTool string `xml:"visualizationTool"`
	RepositoryPath    string `xml:"repositoryPath"`
	OutputPath        string `xml:"outputPath"`
	BranchName        string `xml:"branchName"`
}

func readConfig(filePath string) (Config, error) {
	var config Config
	xmlFile, err := os.Open(filePath)
	if err != nil {
		return config, err
	}
	defer xmlFile.Close()

	decoder := xml.NewDecoder(xmlFile)
	err = decoder.Decode(&config)
	if err != nil {
		return config, err
	}
	return config, nil
}

func getCommits(repoPath, branchName string) (string, error) {

	cmd := exec.Command("git", "log", "--pretty=format:%H|%ad|%an", "--date=iso", branchName)
	cmd.Dir = repoPath

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println("Выполняемая команда:", cmd.String())
		return "", fmt.Errorf("ошибка выполнения git log: %s, вывод ошибки: %s", err, output)
	}

	return string(output), nil
}

func buildGraph(commits string) string {
	lines := strings.Split(commits, "\n")
	var graph strings.Builder
	graph.WriteString("digraph G {\n")

	var lastCommit string

	for i, line := range lines {
		if line == "" {
			continue
		}
		parts := strings.Split(line, "|")
		if len(parts) < 3 {
			continue
		}
		hash := parts[0]
		date := parts[1]
		author := parts[2]

		nodeLabel := fmt.Sprintf("%s\\n%s\\n%s", hash, date, author)
		graph.WriteString(fmt.Sprintf("    \"%s\" [label=\"%s\"];\n", hash, nodeLabel))

		if i > 0 {
			graph.WriteString(fmt.Sprintf("    \"%s\" -> \"%s\";\n", lastCommit, hash))
		}
		lastCommit = hash
	}

	graph.WriteString("}\n")
	return graph.String()
}

func saveGraphToFile(graph, outputPath string) error {
	return os.WriteFile(outputPath, []byte(graph), 0644)
}

func main() {
	configPath := flag.String("config", "config.xml", "Path to the configuration file")
	flag.Parse()

	config, err := readConfig(*configPath)
	if err != nil {
		log.Fatal("Ошибка чтения конфигурационного файла:", err)
	}

	commits, err := getCommits(config.RepositoryPath, config.BranchName)
	if err != nil {
		log.Fatal(err)
	}

	graph := buildGraph(commits)
	err = saveGraphToFile(graph, config.OutputPath)
	if err != nil {
		fmt.Println("Ошибка при сохранении файла:", err)
		os.Exit(1)
	}

	fmt.Println("Граф зависимостей успешно сохранён в", config.OutputPath)
}
