
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
Name                                                       Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------------------
apps/__init__.py                                               0      0   100%
apps/accounts/__init__.py                                      0      0   100%
apps/accounts/admin.py                                         1      0   100%
apps/accounts/api/api_views.py                                14      0   100%
apps/accounts/apps.py                                          4      0   100%
apps/accounts/constants.py                                     4      0   100%
apps/accounts/managers.py                                     12      2    83%   8, 10
apps/accounts/migrations/0001_initial.py                       6      0   100%
apps/accounts/migrations/0002_alter_user_mobile_no.py          4      0   100%
apps/accounts/migrations/__init__.py                           0      0   100%
apps/accounts/models.py                                       25      1    96%   47
apps/accounts/serializers.py                                  37      1    97%   36
apps/accounts/tests.py                                        24      0   100%
apps/accounts/urls.py                                          5      0   100%
apps/contents/__init__.py                                      0      0   100%
apps/contents/admin.py                                         1      0   100%
apps/contents/api/api_views.py                                58      3    95%   43, 69, 79
apps/contents/apps.py                                          4      0   100%
apps/contents/migrations/0001_initial.py                       7      0   100%
apps/contents/migrations/0002_alter_content_category.py        4      0   100%
apps/contents/migrations/0003_alter_content_documents.py       4      0   100%
apps/contents/migrations/__init__.py                           0      0   100%
apps/contents/models.py                                       11      0   100%
apps/contents/serializers.py                                  17      0   100%
apps/contents/tests.py                                        86      0   100%
apps/contents/urls.py                                          4      0   100%
core/__init__.py                                               0      0   100%
core/settings.py                                              30      0   100%
core/urls.py                                                   6      0   100%
manage.py                                                     12      2    83%   12-13
----------------------------------------------------------------------------------------
TOTAL                                                        380      9    98%                 76     10    87%
```

For a nicer presentation, use coverage html to get annotated HTML listings detailing missed lines:

```shell
$ coverage html
```
