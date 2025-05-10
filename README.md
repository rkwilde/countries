# Data Engineering ETL Pipeline Project

## Project Overview
ingest.py calls the API, saves the data in a file, and uploads it to Snowflake. In Snowflake I have a task that brings the important data into staging.
I chose the Countries REST API. Valuable if you're interested in geography.

## Architecture
N/A

### Components
- **Data Extraction**: *Description of how you extract data from the API*
- **Data Transformation**: *Explanation of your transformation logic*
- **Data Loading**: *Details on how data is loaded to the database*
- **Scheduling**: *How you implemented the scheduling mechanism*

## Setup Instructions

### Prerequisites
- Python 3.8+
- Docker (if applicable)
- Any other required tools or services

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your configuration
```

### Database Setup

```bash
# Commands to set up your database
### I used snowflake, so it's already set up, you just need your own values in .env 
```

### Running the Pipeline

```bash
# didn't have time to make a pipeline
# python ingest.py
# execute task countries_transform; # (run in snowflake)
```

### Running with Scheduler/Airflow

```bash
# Instructions for running the pipeline with your scheduler
### didnt' have time for airflow
```

## Data Model
*Describe your data model, including tables, fields, and relationships.*

```sql
-- Example SQL schema
CREATE TABLE APTIVE.RAW.COUNTRIES (
	RAW VARIANT
);
CREATE TABLE APTIVE.STAGING.COUNTRIES (
	COUNTRY_NAME VARCHAR(16777216),
	INDEPENDENT BOOLEAN,
	UNITED_NATIONS_MEMBER BOOLEAN,
	CAPITAL VARCHAR(16777216),
	COUNTRY_REGION VARCHAR(16777216),
	COUNTRY_SUBREGION VARCHAR(16777216),
	POPULATION NUMBER(38,0)
);
```

## Testing

```bash
# Run tests
pytest tests.py  # just one test so far and not very useful
```

## Design Decisions and Assumptions
*Explain any important design decisions you made and assumptions about the data or requirements.*\
N/A

## Scalability Considerations
*Discuss how your solution could scale to handle larger volumes of data or additional data sources.*\
Python and Snowflake both work for big data. Of course what kind of node you run Python on will matter.

## Error Handling and Logging
*Explain your approach to error handling and logging.*\
Tried to have helpful messages for hitting the API. Was rushing by the time I got to the Snowflake uploads so I'm not catching anything there.
Kept logging very simple.

## Future Improvements
*List potential improvements or extensions you would implement with more time.*\
Actually having scheduling, a pipeline, and testing

## License
*Specify your license (e.g., MIT, Apache 2.0)*\
