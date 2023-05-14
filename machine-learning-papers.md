# Questions about Machine Learning Papers

## What are some common use cases for machine learning in practical applications or research prototypes?

Machine Learning(ML) can be used in various fields, the common use cases are: recognition and prediction user activities and gestures (e.g. click through rate of news headlines of a website). ML can also be used to develop wearable system and interactive systems that can intelligently deliver notifications and optimize system resources, such as battery conservation for smartphones. ML also provides the potential to build a complex system quickly. Besides HCI, ML is also useful for hypothesis testing to generate new knowledge about the world. 

## Which problems of machine learning do the authors of the papers identify?
The authors of these two papers also raise a range of problems with ML.
##### From HCI level (Kostakos&Musolesi, 2017):
First, ML prediction accuracy cannot replace the classic hypothesis testing and correlation/causation analysis. ML should not be the basis to answer hypothesis as well, this especially applies to human behaviour analysis such as emotions. Instead of drawing conclusion on results of ML models, researchers should also consider applying more classical statistical methods.

Second, most of the results of ML algorithms provide insights into the relationships of association and not into the relationships of causation, therefore extrapolation from conclusions might also be a problem. 

Third, when conducting uncontrolled experiments, positive behaviour can interfere with systems, so researchers must be very careful when analyzing their findings and drawing conclusions. Also, it's difficult to build control groups as they are crowdsourced or from smartphones from anywhere.

The fourth problem exists in "report", there is little alignment on how HCI researchers report the accuracy of the classifier, and baseline performance should also be reported.

Fifth, it's notable that the accuracy is not enough to evaluate ML classification algorithms. The presence of the false positive can affect the result, and false positive is the result indicates a finding when it actually not.

Sixth, the problem with training data is, trained data for general population might not fit all groups, it is recommended to use clustering to find groups and characteristics.

The seventh problem is that, due to data splitting, ML techniques often capture only part of a phenomenon.
##### From system level (Sculley et. al, 2014):
First, ML packages mix data source together and ML models create entanglement, therefore it can be impossible to make the isolation of improvements effectively. No inputs are really independent, they call this as CACE principle: Changing Anything Changes Everything

Second, hidden feedback loops leads to challenges in analyzing system performance. When a predict model relies on previous prediction to generate new training data, it may take a long time to change its behaviour. Changes that are not immediately visible can add cost even to simple improvements. 

The third problem is undeclared consumers. A prediction from one model can also be used for another model. Undeclared consumers are the consumers without access control and use the prediction of other model as input. Having undeclared consumers is expensive and even dangerous because it may introduce hidden feedback loops.

The fourth problem refers to unstable data dependencies: if the ML input signal depends on other system, it may cause unexpected result

The fifth problem is underutilized data dependencies: packages that are underutilized are mostly unneeded. Underutilized packages provide only little value, but may cause unnecessary changes to the system.

Sixth, it is difficult to perform static data analysis. An additional tool would be needed to track the use of data in a system.

The seventh problem goes to "glue code". Preferring general purpose solution as self-contained packages may lead to "glue code" problems, which can freeze a system to a specific package

The eighth problem is pipeline jungles. Pipeline jungles often happen in data preparation, it can evolve organically when new information added, in this way the preparing data may turn into ML-nonfriendly format.

Finally, using experimental codepaths as condition branches within the main code can affect the system unpredictably over time.

## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?
##### Vassilis Kostakos 
Vassilis Kostakos is the professor of University of Melbourne, he mainly focused on developing intelligent computer systems, which can understand and respond to human behaviour. The systems also include smartphone, a research he published with other authors in 2019 was "Energy-efficient prediction of smartphone unlocking".
See also: https://dl.acm.org/profile/81100283202
https://www.linkedin.com/in/kostakos/
##### Mirco Musolesi
Mirco Musolesi is the Professor of Computer Science at University College London and University Bologna. He also leads the Machine Intelligence Lab. In 2017, he also published other researches on machine learning, such as "Are you getting sick? Predicting influenza-like symptoms using human mobility behaviors".
See also: https://dl.acm.org/profile/81100291777
https://www.mircomusolesi.org/papers/
##### David Sculley
David Sculley worked at Google Research, his subject areas are machine learning, system biology and data mining etc. His researches on machine learning can be found from 2006 to 2022, with the latest research being "Underspecification presents challenges for credibility in modern machine learning".
See also: https://dl.acm.org/profile/81312481321, https://www.linkedin.com/in/d-sculley-90467310/
##### Gary Holt
Gary Holt also works at Google Research. In 2015, he published research along with other authors titled: "Hidden technical debt in Machine learning systems"
See also: https://dl.acm.org/profile/82658766657/publications?Role=author
##### Daniel Golovin
Daniel Golovin is the current lead of Google Brain Group. He works extensively on machine learning and founded an AI platform, Vizier, which can helps with tuning hyperparameters in complex machine learning models.
See also: https://dl.acm.org/profile/81309505145
https://research.google/people/DanielGolovin/
https://cloud.google.com/ai-platform/optimizer/docs/overview
##### Other Authors
Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary and Michael Young were also the co-authors of "Hidden technical debt in Machine learning systems".
See also: 
Eugene Davydov: https://dl.acm.org/profile/81323489333
Todd Phillips: https://dl.acm.org/profile/82659039657
Dietmar Ebner: https://dl.acm.org/profile/99659425157
Vinay Chaudhary: https://dl.acm.org/profile/99659047724
Michael Young: https://dl.acm.org/profile/82658700357