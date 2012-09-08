CHECKPYPATH=../../
export PYTHONPATH=$(CHECKPYPATH)
OUT=out

test: clean
	./check-self -d -o $(OUT) -S ../ $(CHECKPYPATH) testcases/

clean:
	rm -rf $(OUT)
