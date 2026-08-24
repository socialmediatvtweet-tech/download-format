#!/bin/bash

INSTALL_DIR="/usr/local/bin"
BINARY_NAME="osldown"
REPO="socialmediatvtweet-tech/download-format"

echo "Downloading the latest version of osldown from GitHub..."

DOWNLOAD_URL="https://github.com/${REPO}/releases/latest/download/osldown.exe"

if command -v curl &> /dev/null; then
    sudo curl -L -o "${INSTALL_DIR}/${BINARY_NAME}" "${DOWNLOAD_URL}"
elif command -v wget &> /dev/null; then
    sudo wget -O "${INSTALL_DIR}/${BINARY_NAME}" "${DOWNLOAD_URL}"
else
    echo "Error: Neither curl nor wget is installed!"
    exit 1
fi

sudo chmod +x "${INSTALL_DIR}/${BINARY_NAME}"

echo "Done! osldown has been successfully installed."
