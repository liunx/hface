
prompt = """
Summarize the text delimited by triple backticks \
into a single sentence. \
''' \
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs. \
'''
"""

prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres. \
Provide them in JSON format with the following keys: \
book_id, title, author, genre.
"""

prompt = f"""
You will be provided with text delimited by triple quotes. \
If it contains a sequence of instructions, \
re-write those instructions in the following format: \
Step 1 - ... \
Step 2 - ... \
... \
Step N - ... \
If the text does not contain a sequence of instructions, \
then simply write "No steps provided." \
''' \
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy. \
'''
"""

prompt = f"""
Your task is to answer in a consistent style. \
<child>: Teach me about patience. \
<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread. \
<child>: Teach me about resilience.
"""

prod_review = """
Your task is to generate a short summary of a product \
review from an ecommerce site. \
Summarize the review below, delimited by triple backticks, in at most 30 words. \
Review: ``` \
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \
super cute, and its face has a friendly look. It's \
a bit small for what I paid though. I think there \
might be other options that are bigger for the \
same price. It arrived a day earlier than expected, \
so I got to play with it myself before I gave it \
to her. \
```
"""

prompt = """
Your task is to generate a short summary of a product \
review from an ecommerce site. \
Summarize the review below, delimited by triple \
backticks in at most 30 words. \
Review: ``` \
So, they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn’t look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush \
very hard items like beans, ice, rice, etc. in the \
blender first then pulverize them in the serving size \
I want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if I need them finer/less pulpy). Special tip when making \
smoothies, finely cut and freeze the fruits and \
vegetables (if using spinach-lightly stew soften the \
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year, the motor was making a funny noise. \
I called customer service but the warranty expired \
already, so I had to buy another one. FYI: The overall \
quality has gone done in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days. \
```
"""

prompt = f"""
What is the sentiment of the following product review, \
which is delimited with triple backticks? \
Review text: ``` \
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast. \
The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together. \
I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!! \
```
"""

prompt = f"""
Identify the following items from the review text: \
- Item purchased by reviewer \
- Company that made the item \
The review is delimited with triple backticks. \Format your response as a JSON object with \
"Item" and "Brand" as the keys. \
If the information isn't present, use "unknown" \
as the value. \
Make your response as short as possible. \
Review text: ``` \
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast. \
The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together. \
I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!! \
```
"""

system_message = f"""
Follow these steps to answer the customer queries. \
The customer query will be delimited with four hashtags,\
i.e. ####. \
Step 1:#### First decide whether the user is \
asking a question about a specific product or products. \
Product cateogry doesn't count. \
Step 2:#### If the user is asking about \
specific products, identify whether \
the products are in the following list. \
All available products: \
1. Product: TechPro Ultrabook \
Category: Computers and Laptops \
Brand: TechPro \
Model Number: TP-UB100 \
Warranty: 1 year \
Rating: 4.5 \
Features: 13.3-inch display, 8GB RAM, 256GB SSD, Intel Core i5 processor \
Description: A sleek and lightweight ultrabook for everyday use. \
Price: $799.99 \
2. Product: BlueWave Gaming Laptop \
Category: Computers and Laptops \
Brand: BlueWave \
Model Number: BW-GL200 \
Warranty: 2 years \
Rating: 4.7 \
Features: 15.6-inch display, 16GB RAM, 512GB SSD, NVIDIA GeForce RTX 3060 \
Description: A high-performance gaming laptop for an immersive experience. \
Price: $1199.99 \
3. Product: PowerLite Convertible \
Category: Computers and Laptops \
Brand: PowerLite \
Model Number: PL-CV300 \
Warranty: 1 year \
Rating: 4.3 \
Features: 14-inch touchscreen, 8GB RAM, 256GB SSD, 360-degree hinge \
Description: A versatile convertible laptop with a responsive touchscreen. \
Price: $699.99 \
4. Product: TechPro Desktop \
Category: Computers and Laptops \
Brand: TechPro \
Model Number: TP-DT500 \
Warranty: 1 year \
Rating: 4.4 \
Features: Intel Core i7 processor, 16GB RAM, 1TB HDD, NVIDIA GeForce GTX 1660 \
Description: A powerful desktop computer for work and play. \
Price: $999.99 \
5. Product: BlueWave Chromebook \
Category: Computers and Laptops \
Brand: BlueWave \
Model Number: BW-CB100 \
Warranty: 1 year \
Rating: 4.1 \
Features: 11.6-inch display, 4GB RAM, 32GB eMMC, Chrome OS \
Description: A compact and affordable Chromebook for everyday tasks. \
Price: $249.99 \
Step 3:#### If the message contains products \
in the list above, list any assumptions that the \
user is making in their \
message e.g. that Laptop X is bigger than \
Laptop Y, or that Laptop Z has a 2 year warranty. \
Step 4:####: If the user made any assumptions, \
figure out whether the assumption is true based on your \
product information. \
Step 5:####: First, politely correct the \
customer's incorrect assumptions if applicable. \
Only mention or reference products in the list of \
5 available products, as these are the only 5 \
products that the store sells. \
Answer the customer in a friendly tone. \
Use the following format: \
Step 1:#### <step 1 reasoning> \
Step 2:#### <step 2 reasoning> \
Step 3:#### <step 3 reasoning> \
Step 4:#### <step 4 reasoning> \
Response to user:#### <response to customer> \
Make sure to include #### to separate every step. \
User: tell me about the smartx pro phone and \
the fotosnap camera, the dslr one. \
Also tell me about your tvs.
"""

user_message = f"""
by how much is the BlueWave Chromebook more expensive \
than the TechPro Desktop"""