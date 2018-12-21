[![Build Status](https://travis-ci.org/aikrasnov/python-selenium.svg?branch=master)](https://travis-ci.org/aikrasnov/python-selenium)
## How to run UI tests
### Local
0) Install firefox, chrome and put theirs drivers in PATH ([chromedriver](http://chromedriver.chromium.org/), [geckodriver](https://github.com/mozilla/geckodriver/releases))
1) Clone this repo
2) Install pipenv ([instruction](https://github.com/pypa/pipenv#installation))
3) pipenv install --dev
4) pipenv shell
5) pytest

### Sauce Lab
1) Do all the same (except installing drivers)
2) Set environments var SAUCE_USERNAME and SAUCE_ACCESS_KEY
3) pytest

### Change count parallel tests
`pytest -n number`

### View beautiful reports
1) Install allure ([instruction](https://docs.qameta.io/allure/#_installing_a_commandline))
2) Run tests
3) Type `allure generate report --clean && allure open allure-report`

