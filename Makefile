TEMPLATEDIR="template"
DAY=$(shell TZ=America/New_York date '+%d')
DIRNAME="day${DAY}"

.PHONY: all

all:
	@if [ -d $(DIRNAME) ]; then \
		echo "$(DIRNAME) has already existed."; \
	else \
		cp -r $(TEMPLATEDIR) $(DIRNAME); \
		touch "$(DIRNAME)/test.txt" "$(DIRNAME)/data.txt"; \
		mv "$(DIRNAME)/template.py" "$(DIRNAME)/$(DIRNAME).py"; \
		echo "$(DIRNAME) created successfully."; \
	fi
