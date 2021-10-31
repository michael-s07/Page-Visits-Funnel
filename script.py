
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
df=pd.merge(visits,  cart, how='left')
print(df)
print(len(df))

# indicating Null values 
print(df[df.cart_time.isnull()])
print('Visitors whom didnt place a order: '+str(float(len(df[df.cart_time.isnull()]))/float(len(df))*100)+'%')
#There are 82.6% vistiors whom didnt place a order 

#merge df and checkout
df=pd.merge(df,checkout, how ='left')
print('User whom didnt proceed to checkout: '+str(float(len(df[df.checkout_time.isnull()])/float(len(df)))*100)+'%')
# 83.13% users didnt proceed to checkout
all_data= pd.merge(df, purchase, how='left')

print(all_data.head())
print('The users whom didnt proceeded to checkout but didnt purchase a t-shirt are: '+ str(float(len(all_data[all_data.purchase_time.isnull()])/float(len(all_data)))*100)+'%')
all_data['time_to_purchase']=all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())