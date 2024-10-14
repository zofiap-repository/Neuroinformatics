# LINEAR REGRESSION
# Data: learning tasks for subjects with anxiety
# measured with Speilberger Trait Anxiety Inventory (TAI))

from sklearn.linear_model import LinearRegression

X = np.load('X.npy') # TAI 
X = X[:, 1].reshape(-1, 1)
y = np.load('y.npy') # accuracy score 0 - 100% range

model = LinearRegression()
model.fit(X, y)

intercept = model.intercept_ # predicted accuracy when the TAI score is 0 
slope = model.coef_[0]  # predicted accuracy change per unit of TAI
# NEGATIVE SLOPE suggests that higher anxiety is associated with poorer accuracy!

# Print the linear regression model
print(f"Linear Regression Model: Accuracy = {intercept:.2f} + {slope:.2f}*TAI")
x_range = np.linspace(min(X), max(X), 100).reshape(-1, 1)
plt.scatter(X.reshape(-1, 1), y.reshape(-1, 1))
plt.plot(x_range, model.predict(x_range), 'r', label='Regression Line')
plt.ylim(0, 100)
plt.title('Learning Test Results', fontweight='bold', fontsize=18)
plt.xlabel('TAI')
plt.ylabel('Accuracy [%]')
plt.show()

'''
Linear Regression Model: Accuracy = 81.24 + -0.61*TAI
'''