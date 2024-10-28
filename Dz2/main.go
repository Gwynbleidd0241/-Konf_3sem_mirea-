package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/xml"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
	"time"
)

type Config struct {
	VisualizationTool string `xml:"visualizationTool"`
	RepositoryPath    string `xml:"repositoryPath"`
	OutputPath        string `xml:"outputPath"`
	BranchName        string `xml:"branchName"`
}

type Commit struct {
	Hash   string
	Date   string
	Author string
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

func generateCommits() []Commit {
	authors := []string{"Gwynbleidd0241"}
	var commits []Commit

	for i := 0; i < 10; i++ {
		author := authors[i%len(authors)]
		date := time.Now().AddDate(0, 0, -i).Format("2006-01-02 15:04:05")

		hash := generateHash(fmt.Sprintf("%s|%s|%d", author, date, i))
		commits = append(commits, Commit{Hash: hash, Date: date, Author: author})
	}

	return commits
}

func generateHash(data string) string {
	hash := sha256.Sum256([]byte(data))
	return hex.EncodeToString(hash[:])
}

func buildGraph(commits []Commit) string {
	var graph strings.Builder
	graph.WriteString("digraph G {\n")

	var lastCommit string

	for i, commit := range commits {
		nodeLabel := fmt.Sprintf("%s\\n%s\\n%s", commit.Hash, commit.Date, commit.Author)
		graph.WriteString(fmt.Sprintf("    \"%s\" [label=\"%s\"];\n", commit.Hash, nodeLabel))

		if i > 0 {
			graph.WriteString(fmt.Sprintf("    \"%s\" -> \"%s\";\n", lastCommit, commit.Hash))
		}
		lastCommit = commit.Hash
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

	commits := generateCommits()

	graph := buildGraph(commits)
	err = saveGraphToFile(graph, config.OutputPath)
	if err != nil {
		fmt.Println("Ошибка при сохранении файла:", err)
		os.Exit(1)
	}

	fmt.Println("Граф зависимостей успешно сохранён в", config.OutputPath)
}
