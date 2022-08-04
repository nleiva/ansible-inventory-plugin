.DEFAULT_GOAL := help

.EXPORT_ALL_VARIABLES:

.PHONY: build

all: build

build: check-env ## Build and upload to Galaxy. Make sure you TAG correctly
	sed -i "s/version:.*/version: ${TAG}/" galaxy.yml
	sed -i "s/version:.*/version: ${TAG}/" README.md
	git add .
	git commit -m "Bump to version ${TAG}"
	git tag -a -m "Bump to version ${TAG}" v${TAG}
	git push --follow-tags
	ansible-galaxy collection build
	ansible-galaxy collection publish ./nleiva-inventory-${TAG}.tar.gz

check-env: ## Check if TAG variable is set. Brought to you by https://stackoverflow.com/a/4731504
ifndef TAG
	$(error TAG is undefined)
endif
	@echo "TAG is ${TAG}"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'