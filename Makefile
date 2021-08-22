.PHONY: clean test
clean:	
		rm -rf before_process after_process
test:
		mkdir before_process after_process result_files
