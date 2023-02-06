all: verify

.PHONY: help
help:
	@awk -f ./hack/help.awk $(MAKEFILE_LIST)

##@ code

.PHONY: verify
verify: format lint  ## run all verifications

.PHONY: format
format: ## run formatter
	$(MAKE) -s _docker_$@

.PHONY: lint
lint: ## run linter
	$(MAKE) -s _docker_$@

##@ artifact

.PHONY: docs
docs:  ## generate documentation
	$(MAKE) -s _$@

##@ general

_docker_%:
	docker-compose build test && docker-compose run --rm test make _$*

_%:
	./hack/$*.sh
