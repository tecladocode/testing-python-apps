# Set up

We'll need a few things to install for this section:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```

If you want to run the tests in PyCharm, you'll need to create appropriate configurations. We cover this in the course!