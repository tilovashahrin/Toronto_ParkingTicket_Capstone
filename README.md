## Toronto Parking Ticket Data Capstone

**Dataset**: This dataset, available on Open Toronto's website, contains information about parking tickets issued in the city of Toronto from 2012 to 2022. It includes details such as the ticket issuance date, location, violation type, and fine amount. With approximately 2 million rows of data per year, this dataset provides a comprehensive record of parking violations in Toronto over a ten-year period.
https://open.toronto.ca/dataset/parking-tickets/

**Author**: Tilova Shahrin

**Contact**: tilova97@gmail.com

### **Project Overview**: 
My interest is focused on analyzing parking tickets in the city of Toronto, which falls under the broader field of urban data analysis. 

### **Problem Area**

Resource Allocation - Understanding where and when parking violations occur most frequently is crucial for optimizing resource allocation for enforcement laws and efforts.

1. Analyze any patterns of parking violations to identify peak times and days of the week when violations are most shown. This analysis can help the city schedule enforcement patrols more efficiently, finding when and where they are most needed.
2. Using mapping analysis to identify hotspots of parking violations within the city. Pinpointing areas with high concentrations of violations, the city can prioritize enforcement efforts in these locations to maximize effectiveness.
3. Developing predictive models based on historical data to forecast future parking violation hotspots. By leveraging factors such as time of day, day of the week, events, and other relevant variables, these models can help the city proactively allocate resources and plan enforcement strategies.

### **Users**

Residents 
- Residents in different neighborhoods may experience discrepancy in parking enforcement, with some areas facing more frequent ticketing than others. This could lead to feelings of unfair
treatment, mostly if enforcement practices appear biased or inequitable. Residents across all neighborhoods stand to benefit from a more transparent and fair parking enforcement system.

Communities affected by unequal enforcement 
- Communities that often get hit harder with parking tickets would endure more fines. Hence
more financial stress from piling up tickets, making it tougher to afford other things. Plus, increased enforcement could make it trickier for residents in these areas to get to important places like work or the grocery store.

### **Dataset Description**

| Column                 | Description                                                                                       |   
|------------------------|---------------------------------------------------------------------------------------------------|
| Tag Number Masked      | Ticket ID of the individual row, half the ID is masked for privacy purposes.                      | 
| Date of Infraction     | Date of which the ticket was issued.                                                              |  
| Infraction Code        | The code number for the type of parking offence.                                                  |  
| Infraction Description | Description of the parking offence type.                                                          |  
| Set Fine Amount        | The total fine amount for the offence.                                                            | 
| Time of Infraction     | Time of which the parking offence occured.                                                        |  
| Location 1             | Speicification of where the car was located based on address (At, On, South Side, West Side etc.) |  
| Location 2             | Address of parking offence.                                                                       |   
| Location 3             | Speicification of where the car was located based on address (North of, East of, etc.)            |   
| Location 4             | Address of parking offence. Possibly a intersection from location 1.                              |  
| Province               | Province of vehicle liscense plate.                                                               | 

## Project Files Breakdown

### Docs
- **Sprint0_Tilova_Shahrin.pdf**: Documentation for Sprint 0, outlining project goals, scope, and initial planning.
- **Sprint1_Presentation_TilovaShahrin.pdf**: Presentation slides for Sprint 1, covering progress, challenges, and next steps.
- **Sprint2_Presentation_TilovaShahrin.pdf**: Presentation slides for Sprint 2, highlighting further progress, results, and future plans.

### Notebooks
- **.ipynb_checkpoints**: Checkpoint directory automatically generated by Jupyter Notebook.
- **1. Cleaning and EDA.ipynb**: Notebook focusing on data cleaning and exploratory data analysis (EDA) tasks.
- **2. Feature Engineering, Preprocessing and EDA.ipynb**: Notebook dedicated to feature engineering, preprocessing, and further EDA.
- **3. Modeling.ipynb**: Notebook containing initial modeling efforts and evaluation.
- **4. Advanced Modeling.ipynb**: Notebook exploring advanced modeling techniques, hyperparameter tuning, and model optimization.

### README.md
- **README.md**: Main documentation file providing an overview of the project, its components, and instructions for setup and usage.

### Environment Configuration
- **myenv.yml**: YAML file specifying the environment configuration, including dependencies and package versions, for reproducibility and ease of setup.

## Solution Impact: Enhancing Parking Enforcement Efficiency

The implementation of predictive modeling in parking enforcement has the potential to significantly impact urban mobility and management. Here are some key ways in which my solution can make a difference:

#### 1. Improved Resource Allocation:
By accurately predicting areas with a higher likelihood of parking violations, parking enforcement authorities can allocate their resources more efficiently. This targeted approach ensures that enforcement efforts are focused where they are most needed, optimizing manpower and reducing operational costs.

#### 2. Enhanced Safety:
Illegal parking in restricted zones such as fire lanes or pedestrian crossings poses significant safety risks. This solution promotes safer streets and reduces the likelihood of accidents and emergencies, ultimately enhancing public safety and well-being.

#### 3. Positive Environmental Impact:
Efficient parking enforcement contributes to the reduction of vehicle emissions and environmental pollution by minimizing unnecessary traffic congestion and idling. By promoting smoother traffic flow and reducing the time spent searching for parking, this supports environmental sustainability efforts and promotes greener, more eco-friendly cities.

#### 4. Enhanced User Experience:
For drivers, my solution offers a more seamless and convenient parking experience by reducing the frustration associated with illegal parking and congestion. This contributes to a positive urban environment where residents and visitors can navigate the city with ease and confidence.

#### Empowering Sustainable Urban Mobility:
By harnessing the capabilities of predictive modeling, I contribute to the advancement of sustainable urban mobility initiatives. My efforts aim to optimize parking enforcement practices, reduce congestion, enhance safety, and ultimately create more livable and accessible urban environments for all.

### Streamlit Demo: Interactive Web Application

The project includes an interactive web application built with Streamlit, a popular Python library for creating data-driven web applications. The Streamlit demo provides a user-friendly interface for exploring the predictive models and visualizing their results.

**Features**
1. Model Prediction: Users can input location data and receive predictions for potential parking violations and associated fines.
2. Visualization: The application includes interactive visualizations to enhance understanding and interpretation of the model predictions.
3. User-Friendly Interface: Streamlit's intuitive interface makes it easy for users to interact with the application and obtain insights from the predictive models.

**Demo Recording**

### Setup
The project includes a YAML file named myenv.yml, which specifies the required dependencies and package versions for reproducibility.
[streamlit-main-2024-04-23-16-04-62.webm](https://github.com/tilovashahrin/Toronto_ParkingTicket_Capstone/assets/46762829/ab9f9831-e3b1-40ed-88b2-ea131885f218)

1. Clone the Repository: Start by cloning this repository to your local machine using Git.
2. Create Conda Environment: Navigate to the project directory and create a new Conda environment using the provided YAML file.
3. Activate Environment: Activate the newly created Conda environment.
4. Launch Jupyter Notebook: Launch Jupyter Notebook to explore the project notebooks.

Additional Notes:

Ensure that you have Anaconda or Miniconda installed on your system before proceeding with the environment setup.
If you encounter any issues during the setup process, please refer to the project documentation or reach out to the project team for assistance.
