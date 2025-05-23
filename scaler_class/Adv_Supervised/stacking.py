import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import RepeatedKFold

from sklearn.model_selection import cross_val_score



X = np.asarray([[-0.12289022551864817, -0.9357694342590688], [0.5129298204180088, -0.29809283510271567], [0.48851814653749703, -0.07557171302105573], [-0.2678880796260159, 0.530355466738186], [-1.1006191772129212, 1.1447237098396141], [-1.4441138054295894, -0.5044658629464512], [0.8389834138745049, 0.9311020813035573], [-0.17242820755043575, -0.8778584179213718], [0.2300947353643834, 0.7620111803120247], [-0.671246130836819, -0.01266459891890136], [-0.6871727001195994, -0.8452056414987196], [0.31903909605709857, -0.2493703754774101], [-0.691660751725309, -0.39675352685597737], [-0.7471582937508376, 1.6924546010277466], [1.6598021771098705, 0.7420441605773356], [-0.6200008439481293, 0.6980320340722189], [-0.3752849500901142, -0.6387304074542224], [-0.3062040126283718, 0.8279746426072462], [-0.3224172040135075, -0.38405435466841564], [1.74481176421648, -0.7612069008951028], [0.8654076293246785, -2.3015386968802827], [0.12015895248162915, 0.6172031097074192], [-0.22232814261035927, -0.20075806892999745], [-0.7543979409966528, 1.2528681552332879], [1.6243453636632417, -0.6117564136500754], [-1.1173103486352778, 0.23441569781709215], [-0.5281717522634557, -1.0729686221561705], [0.9015907205927955, 0.5024943389018682], [0.4234943540641129, 0.07734006834855942], [0.3001703199558275, -0.35224984649351865], [-0.19183555236161492, -0.8876289640848363], [0.04221374671559283, 0.5828152137158222], [0.16003706944783047, 0.8761689211162249], [0.19829972012676975, 0.11900864580745882], [1.131629387451427, 1.5198168164221988], [2.1855754065331614, -1.3964963354881377], [1.462107937044974, -2.060140709497654], [1.198917879901507, 0.18515641748394385], [0.1865613909882843, 0.4100516472082563], [0.19091548466746602, 2.100255136478842], [1.1337694423354374, -1.0998912673140309], [-0.6706622862890306, 0.3775637863209194], [-1.1425181980221402, -0.3493427224128775], [-0.3438536755710756, 0.04359685683424694], [0.9008559492644118, -0.6837278591743331], [-0.2088942333747781, 0.5866231911821976], [0.05080775477602897, -0.6369956465693534], [0.31563494724160523, -2.022201215824003], [0.12182127099143693, 1.1294839079119197], [0.2855873252542588, 0.8851411642707281]] )
y = np.asarray([-46.34457583853899, 29.89203815293042, 36.57670478050099, -1.0548543507733465, -44.34760203047087, -136.23585513274503, 103.81048050179038, -48.10275508775748, 48.11630577045144, -54.62694386929622, -88.13212433240432, 16.15177140411067, -71.37438371388818, 5.53682925172843, 162.66695252711517, -23.210158588999548, -55.040032571465225, 7.3813358866864425, -40.945038837952694, 111.31738238616813, -19.52961992002634, 33.79973612507111, -25.64394667923562, -12.417030626190087, 107.41448375249622, -81.08909809239485, -84.1858887757812, 92.17168168963711, 37.248421360886816, 10.59831841709924, -49.78340567852572, 26.043717785494916, 46.98000533279682, 20.673696974050426, 150.21975566743365, 122.28638742509285, 38.00737094940657, 104.00861175886935, 31.03679755941446, 96.99313535634106, 48.849928674845266, -39.47151812217092, -105.88279350591996, -26.092669988864273, 46.22449353100841, 5.979177298086575, -20.791632075145184, -52.9535092860866, 53.64827578648195, 57.32065154495446])

# get a stacking ensemble of models
def get_stacking():
	# define the base models
	level0 = list()
	level0.append(('knn', KNeighborsRegressor()))
	level0.append(('cart', DecisionTreeRegressor()))

	# define meta learner model, it'll be a linear regression model
	level1 = LinearRegression()
	
	# define the stacking ensemble for regression with level0 and meta model
	model = StackingRegressor(estimators=level0, final_estimator=level1)
	
	return model

# get a list of models to evaluate
def get_models():
	models = dict()
	
	#intialize the object for knn for regression
	models['knn'] = KNeighborsRegressor()
	
	#intialize the object for decision tree for regression
	models['cart'] = DecisionTreeRegressor()
	models['stacking'] = get_stacking()
	
	return models

# evaluate a given model using cross-validation
def evaluate_model(model, X, y):

    #initialize RepeatedKfold object with k = 10 and 3 repetitions
	cv = RepeatedKFold(n_splits=10, n_repeats=3)
	
	# evaluate the model using r2 and the above cross validation strategy
	scores = cross_val_score(model, X, y, scoring='r2', cv = cv)
	
	return scores


# get the models to evaluate
models = get_models()

# evaluate the models and store results
results, names = list(), list()

for name, model in sorted(models.items()):
	scores = evaluate_model(model, X, y)
	results.append(scores)
	print('%s %.3f' % (name, np.mean(scores)))