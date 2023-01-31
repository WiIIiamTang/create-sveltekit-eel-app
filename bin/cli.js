#!/usr/bin/env node

import inquirer from "inquirer";
import * as fs from "fs";
import { dirname } from "path";
import { fileURLToPath } from "url";
import createDirectoryContents from "./createDirectoryContents.js";
import { execSync } from "child_process";
const CURR_DIR = process.cwd();
const __dirname = dirname(fileURLToPath(import.meta.url));

const CHOICES = fs.readdirSync(`${__dirname}/../templates`);

const QUESTIONS = [
  {
    name: "project-choice",
    type: "list",
    message: "What project template would you like to generate?",
    choices: CHOICES,
  },
  {
    name: "project-name",
    type: "input",
    message: "Project name:",
    validate: function (input) {
      if (/^([A-Za-z\-\\_\d])+$/.test(input)) return true;
      else
        return "Project name may only include letters, numbers, underscores and hashes.";
    },
  },
  {
    // init git prompt
    name: 'git',
    type: 'confirm',
    message: 'Initialize a git repository?',
  },
  {
    // install deps
    name: 'install',
    type: 'confirm',
    message: 'Install dependencies with npm install?',
  }
];

inquirer.prompt(QUESTIONS).then((answers) => {
  const projectChoice = answers["project-choice"];
  const projectName = answers["project-name"];
  const templatePath = `${__dirname}/../templates/${projectChoice}`;

  fs.mkdirSync(`${CURR_DIR}/${projectName}`);

  createDirectoryContents(templatePath, projectName);

  // init git if they said yes
  if (answers.git) {
    execSync('git init', { cwd: `${CURR_DIR}/${projectName}`, stdio: 'inherit' });
  }

  // install deps if they said yes
  if (answers.install) {
    execSync('npm install', { cwd: `${CURR_DIR}/${projectName}`, stdio: 'inherit' });
  }

  console.log("\nYour project was created successfully! Get started with:\npip3 install -r requirements.txt\nnpm i\nnpm run start:eel");
});
