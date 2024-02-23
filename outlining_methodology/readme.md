1. Problem Statement
- What question or questions are you focused on answering?
In recent years, have efforts to reduce food waste made a significant impact on the amount of food waste being produced?

- What is your expected outcome? (i.e. what will you be predicting or analyzing?)
I plan on predicting the amount of food that goes to waste based on various other factors related to food production and usage.

- Can you use this problem statement to create a narrative or story that will guide your presentation?
This problem statement can be used to create a narrative around the impacts of food waste and the impact that less food waste would have.

2. Dataset(s)
- List dataset sources
I'll be gathering dataset sources on either a state or national level from https://insights-engine.refed.org/food-waste-monitor?view=overview&year=2016. The listed dataset is from 2016, but they have datasets from 2016 to 2022 with ample data.

- If working with multiple data sources/datasets, note how you will be combining them.
As these are technically all different datasets that I'll be using, but they are all from the same organization with the same variables, I'll be merging them column-for-column.

- Outline any cleaning or transformation steps you expect to take. Are any of these industry or subject-specific?
I expect to be removing a significant portion of columns that may not be relevant to the question or pertain to the subject at a level beyond my understanding.

- Detail any requisite assumptions you need to check or transformations that must occur for the models you plan on applying. Be specific with which techniques you are interested in.
I'll need to investigate and identify any outliers in the data for my linear regression model, but I am not sure of what transformation I will use on the data in this instance as I do not expect any particularly notable outliers.

3. Modeling
- What is (are) your target(s)?
My target is the amount of food wasted.

- Name at least 3 models that you could explore, given your target.
Linear regression, SVR, and random forest regressor
  - Are those supervised or unsupervised?
  Supervised

  - Do you have any expectations on performance? If so, why?
  Given how robust and large my dataset(s) are, I anticipate fairly good performance.

- What are some of the benefits and shortcomings of those models?
Linear regression allows for exceptional ease of interpretation, but it can also be fairly simplistic and may not lend itself to as detailed tuning as other models.
Admittedly, linear regression is my primary model I'll be focusing on, but I plan on looking into the documentation for other models (likely more than just SVR and RF Regressor) to see if I can tune other models more closely based on the results that I receive with linear regression.

- Are there there assumptions about your target that must be met for those models? If yes, go back into section 1 and make note
Linear regression *could* be impacted strongly by outliers depending on the extremity of the outliers, but in such a large dataset, that may not make a significant impact.

- Are there any assumptions to confirm or requisite steps to take with your independent variables for those models? If yes, go back into section 1 and make note.
Based on the understanding that I have of the features that I have observed in my datasets, I don't anticipate any particular transformations needing to be done.

4. Resources / References
- Gather any references and resources you are looking to use in your project.
- These can be related to the subject matter or methods you are looking to apply.
- Stick to verified resources such as peer-reviewed journals, government and educational platforms, and lauded industry experts.
- This section may not be filled out until further along in your project!