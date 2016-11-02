# {{cookiecutter.project_name}}
{{cookiecutter.description}}

## Project organization

    ├── README.md          <- The top-level README for analists using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data frame for modeling.
    │   └── raw            <- Optional: The original, immutable data dump.
    │                         Preferably empty as we load from the read-only data lake in /mnt/data/
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, papers, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── requirements.txt   <- Optional: the requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`. This can also be an 
    │                         environment.yml file for conda environments.
    │
    └── src                <- Source code for use in this project.
        │
        ├── data           <- Scripts to download or generate data.
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │                     predictions.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.

Project based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/) #cookiecutterdatascience
