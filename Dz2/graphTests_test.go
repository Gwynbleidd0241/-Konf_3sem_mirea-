package main

import (
	"os"
	"testing"
)

func TestReadConfig(t *testing.T) {
	configContent := `<?xml version="1.0" encoding="UTF-8"?>
<config>
    <visualizationTool>/opt/homebrew/bin/dot</visualizationTool>
    <repositoryPath>/Users/gwynbleidd/Desktop/2nd homework/Java</repositoryPath>
    <outputPath>/Users/gwynbleidd/Desktop/2nd homework/files/output.dot</outputPath>
    <branchName>master</branchName>
</config>`
	tmpFile, err := os.CreateTemp("", "config.xml")
	if err != nil {
		t.Fatalf("Ошибка при создании временного файла: %v", err)
	}
	defer os.Remove(tmpFile.Name())

	if _, err := tmpFile.WriteString(configContent); err != nil {
		t.Fatalf("Ошибка записи в файл: %v", err)
	}
	tmpFile.Close()

	config, err := readConfig(tmpFile.Name())
	if err != nil {
		t.Fatalf("Ошибка чтения конфигурационного файла: %v", err)
	}

	if config.VisualizationTool != "/opt/homebrew/bin/dot" {
		t.Errorf("Ожидалось '/opt/homebrew/bin/dot', получено '%s'", config.VisualizationTool)
	}
	if config.RepositoryPath != "/Users/gwynbleidd/Desktop/2nd homework/Java" {
		t.Errorf("Ожидалось '/Users/gwynbleidd/Desktop/2nd homework/Java', получено '%s'", config.RepositoryPath)
	}
	if config.OutputPath != "/Users/gwynbleidd/Desktop/2nd homework/files/output.dot" {
		t.Errorf("Ожидалось '/Users/gwynbleidd/Desktop/2nd homework/files/output.dot', получено '%s'", config.OutputPath)
	}
	if config.BranchName != "master" {
		t.Errorf("Ожидалось 'master', получено '%s'", config.BranchName)
	}
}

func TestBuildGraph(t *testing.T) {
	commits := []Commit{
		{Hash: "hash1", Date: "2023-01-01 00:00:00 +0000", Author: "Author1"},
		{Hash: "hash2", Date: "2023-01-02 00:00:00 +0000", Author: "Author2"},
	}
	expectedGraph := `digraph G {
    "hash1" [label="hash1\n2023-01-01 00:00:00 +0000\nAuthor1"];
    "hash2" [label="hash2\n2023-01-02 00:00:00 +0000\nAuthor2"];
    "hash1" -> "hash2";
}
`
	graph := buildGraph(commits)

	if graph != expectedGraph {
		t.Errorf("Ожидалось %s, получено %s", expectedGraph, graph)
	}
}

func TestSaveGraphToFile(t *testing.T) {
	graph := "digraph G {}"
	tmpFile, err := os.CreateTemp("", "output.dot")
	if err != nil {
		t.Fatalf("Ошибка создания временного файла: %v", err)
	}
	defer os.Remove(tmpFile.Name())

	err = saveGraphToFile(graph, tmpFile.Name())
	if err != nil {
		t.Fatalf("Ошибка сохранения графа в файл: %v", err)
	}

	content, err := os.ReadFile(tmpFile.Name())
	if err != nil {
		t.Fatalf("Ошибка чтения временного файла: %v", err)
	}
	if string(content) != graph {
		t.Errorf("Ожидалось %s, получено %s", graph, content)
	}
}
