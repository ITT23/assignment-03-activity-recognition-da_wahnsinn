# Questions about Machine Learning Papers

## What are some common use cases for machine learning in practical applications or research prototypes?

Machine Learning(ML) can be used in various fields, the common use cases are: recognition and prediction user activities and gestures (e.g. click through rate of news title of a website). ML can also be used to develop wearable system and interactive systems that can intelligently deliver notifications and optimise system resources, such as battery conservation for smartphones. ML also provides the potential to build a complex system quickly. Besides HCI, ML is also useful for hypothesis testing to generate new knowledge about the world. With ML a complex system can be built quickly. 

# Avoiding Pitfalls in Using Machine Learning in HCI Studies
# activity recognition & wearable computing
- model human behaviour (also individual persons)
# Machine Learning: The High-Interest Credit Card of Technical Debt
- with user click data of a website, click through rate(CTR) of news headlines can be predicted

## Which problems of machine learning do the authors of the papers identify?
Authors of these two papers also raise many problems with ML.
From application level (Kostakos&Musolesi, 2017):
First, ML prediction accuracy cannot replace the classic hypothesis testing and correlation/causation analysis. ML should not be the basis to answer hypothesis as well, this especially applies on human behaviour analyse such as emotions. Instead of drawing conclusion on results of ML models researchers should also consider to apply more classical statistical methods.

Second, most of the results of ML algorithms provide insights into the relationships of association and not into the relationships of causation, therefore extrapolation from conclusions might also be a problem. 

Third, when conducting uncontrolled experiments, positive behaviour can interfere with systems, so researchers must be very careful when analysing their findings and drawing conclusions. Also it's difficult to build controll groups as they are crowdsourced or from smartphones from anywhere.

The fourth problem exists in "report", there is little alignment on how HCI researchers report the accuracy of the classifier, and baseline performance should also be reported.

Fifth, it's notable that the accurancy is not enough to evaluate ML classification algorithmus. The presence of the false positive can affect the result, and false positive is the result indicates a finding when it actually not.

Sixth, the problem with training data is, trained data for general population might not fit all groups, it is recommened to use clustering to find groups and characteristics.

The seventh problem is that, due to data splitting, ML techniques often capture only part of a phenomenon.

# Avoiding Pitfalls in Using Machine Learning in HCI Studies
# performance of ML models must be evaluated for their effectivenes, efficiency and complexity. There is no common guideline to report accuracy and their relation to the baseline performance. also the sensivity of classifiers and different threshold should be considered (ROC). false-positives are also important. 

# - Although the interpretation of deep learning algorithm output is an area of intense research, the current available tools provide limited information about the “inner workings” of the models
# complexity of models (researcher must be trained on their basics to draw the correct conclusions)

# Machine Learning: The High-Interest Credit Card of Technical Debt
From system level (Sculley et. al, 2014):
First, ML packages mix data source together and ML models create entanglement, therefore it can be impossible to make the isolation of improvements effectively. No inputs are really independent, they call this as CACE principle: Changing Anything Changes Everything

Second, hidden feedback loops leads to challenges in analyzing system performance. When a predict model relies on previous prediction to generate new training data, it may take a long time to change its behaviour. Changes that are not immediately visible can add cost even to simple improvements. 

The third problem is undeclared consumers. A prediction from one model can also be used for another model. Undeclared consumers are the consumers without access control and use the prediction of other model als input. Having undeclared consumers is expensive and even dangerous because it may introduce hidden feedback loops.

The fourth problem refers to unstable data dependencies: if the ML input signal depends on other system, it may cause unexpected result

The fifth problem is underutilized data dependencies: packages that are underutilized are mostly unneeded. Underutilized packages provide only little value but may cause unnecessary changes to system.

Sixth, it is difficult to perform static data analysis. An additional tool would be needed to track the use of data in a system.

The seventh problem goes to "glue code". Prefering general purpose solution as self-contained packages may lead to "glue code" problems, which can freeze a system to a specific package

The eighth problem is pipeline jungles. Pipeline jungles often happens in data preparation, it can evolve organically when new information added, in this way the preparing data may turned into ML-nonfriendly format.

Finally, using experimental codepaths as condition branches within the main code can affect the system in an unpredictable way over time.

## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?
Vassilis Kostakos: https://dl.acm.org/profile/81100283202
Mirco Musolesi: https://dl.acm.org/profile/81100291777

David Sculley: https://dl.acm.org/profile/81312481321
Gary Holt: https://dl.acm.org/profile/82658766657
Daniel Golovin: https://dl.acm.org/profile/81309505145
Eugene Davydov: https://dl.acm.org/profile/81323489333
Todd Phillips: https://dl.acm.org/profile/82659039657
Dietmar Ebner: https://dl.acm.org/profile/99659425157
Vinay Chaudhary: https://dl.acm.org/profile/99659047724
Michael Young: https://dl.acm.org/profile/82658700357