
## Installation

    Python 3.x is required. If you don't have Python 3.x or higher, download the appropriate package and install:

* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/Shehbaazsk/Contnent-Management-System-API.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd core
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python3 -m venv venv
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```

## Testing
 

To start the tests, simply run:
```shell
python3 manage.py test
```

You should see the following output:

```shell
python3 manage.py test
Creating test database for alias 'default'...
...
----------------------------------------------------------------------
Ran .....

OK
Destroying test database for alias 'default'...
```
### Code Coverage

The 'coverage' module is also available to provide a report of how well your Django project is covered by unit tests. 

To create a coverage report, simply run:

```shell
coverage run manage.py test
```

Afterwards, you can view the report by:

```shell
$ coverage report -m
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
my_program                   20      4    80%   33-35, 39
my_other_module              56      6    89%   17-23
-------------------------------------------------------
TOTAL                        76     10    87%
```

For a nicer presentation, use coverage html to get annotated HTML listings detailing missed lines:

```shell
$ coverage html
```