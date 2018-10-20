# CS 5513 Distributed Database (Spring 2016)

Implement distributed database in MongoDB

## Description

Read the following scenario, and then, perform the tasks explained below using MongoDB. 
 
Suppose that the store MySears sells a wide range of products and has decided to acquire an online presence that could allow MySears to sell products on the web. For this purpose, MySears has bought 3 sites (computer nodes): gpel8.cs.ou.edu, gpel9.cs.ou.edu, and gpel10.cs.ou.edu.  The idea of the MySears managers is to provide its potential customers extensive information about the products they sell. The file catalog.txt contains MySears’s catalog. The managers want you to create the database backend for a catalog system (using MongoDB) using the three sites, and ensure that the catalog is highly available and flexible so that product types can be deleted and inserted at any time without having to bring the system down, and so that even in the face of network failures users can still access portions of the catalog.  The catalog is expected to contain a large number of different product types over time.  The managers tell you that the following queries will be frequently issued:

1. Insert a product into the catalog.

2. Retrieve 30 products from the catalog.

3. Retrieve the top 30 products that have the highest discount rates.

4. Retrieve all the digital cameras made by a particular brand that have a regular price in a given price range.

5. Retrieve all computers in the catalog that are equipped with SSD drives larger than a given ‘hdd\_size’ and that have Windows 8.1 or Windows 10.

6. Delete all televisions in the catalog that have a resolution lower than a given value. 
 
Every product has a unique product ID (product\_id). The product types and their corresponding attributes that must be available in the catalog at the time of implementation are the following, where attributes of the form attribute_name(attr\_1, attr\_2,…) denote composite attributes, and attribute_name{…} denote multi-value attributes: 
 
* **Television**: product_type, product_id, price(regular_price, discount_price), shipping_size(length, width, depth), brand, size, type, three_d, frequency, resolution, input_lag, inputs{…}.
    
    Example entry in the catalog:

      television,127,1940.19,1746.17,69.25,48.75,15.12,RCA,55in ,SmartTV,3D,120Hz,720p,23ms,{USB,HDMI}

* **Computer\_monitor**: product\_type, product\_id, price(regular\_price, discount\_price), shipping\_size(length, width, depth), brand, size, type, frequency, resolution, input\_lag.
  
    Example entry in the catalog:

      computer_monitor,102,318.50,256.65,Sharp,20in,No 3D,120Hz,1080p,20ms

* **Desktop\_computer**: product\_type, product\_id, price(regular\_price, discount\_price), shipping\_size(length, width, depth), brand, num_cores, hard_drive(product\_id, brand, rpm, hdd\_type, hdd\_size, form\_factor, cache\_size, interface), computer\_monitor(product\_id, brand, size, type, frequency, resolution, input\_lag), battery\_duration, OS, peripherals{…}.

    Example entry in the catalog: 

      desktop_computer,103, 5618.50,5056.65,18.80,17.53,10.84,Acer,6cores,10in,Noteb ook,hard_drive,Intel,7200rpm,HDD/SSD,250GB,laptop,128MB, SATA3,Regular,computer_monitor,Sharp,20in,No 3D,120Hz,1080p,20ms,2hr,Spanish,Windows 10,{mouse,keyboard,speakers}

* **Hard\_drive**: product\_type, product\_id, price(regular\_price, discount\_price), shipping\_size(length, width, depth), brand, rpm, hdd\_type, hdd\_size, form\_factor, cache\_size, interface.

    Example entry in the catalog:

      hard_drive,77,355.56,320.00,4.51,4.86,0.81,Toshiba,5400rp m,HDD,120GB,laptop,64MB

* **Digital\_camera**: product\_type, product\_id, price(regular\_price, discount\_price), shipping\_size(length, width, depth), brand, megapixels, sensor\_size, max\_iso, memory\_card\_type, camera\_type, viewfinder(viewfinder\_construction, coverage, eye\_relief), frames\_per\_second, num\_focus\_points, focal\_length, min\_aperture.

    Example entry in the catalog:

      digital_camera,106,26385.86,23747.28,10.51,10.87,7.90,C anon,16MP,Medium Format,25600,SD,DSLR,Pentaprism,0.5,17mm,5fps,160,35,3. 5 
 
## Tasks

1) Create a single collection ‘product’. Do not create a collection for every product\_type.

2) For efficient processing of the catalog queries mentioned above, explain in detail which indexes are needed and why. Then, create those indexes using MongoDB.

3) Insert the products into the catalog.  To do this, perform the following sub-tasks:

        a. Using the programming language of your preference (Java, Python, etc.), write a program ‘txt\_parser’ that takes the given file catalog.txt (available on the class website) containing the product data as input, and then generate a MongoDB script named ‘catalogInsertion.txt’ that contains the MongoDB commands to insert every product entry (not product\_type) into the catalog
    
        b. Run the ‘catalogInsertion.txt’ script in MongoDB to insert products into your catalog. 
 
4) Implement the queries (2-6) using only the MongoDB query language (not Java, Python or any other programming languages).  Run each of the queries (2-3) one time each and run the queries (4-5) three times each. Provide screenshots of the output of each run.

5) Run query (6) two times. Provide screenshots of the output of each run.

6) Design a suitable horizontal partitioning (sharding) scheme to answer the above queries (2-5) that uses the three machines gpel8.cs.ou.edu, gpel9.cs.ou.edu and gpel10.cs.ou.edu.  You need to describe and justify your sharding design in detail. Then, implement your horizontal partitioning design in MongoDB. Your implementation must include the code to set up the horizontal partitioning scheme. For this task you only need to implement your sharding scheme. You do not need to implement replication in this task. You also need to provide a screenshot of the output of the command rs.status() when you run it in your replica set; this is to ensure that your replica set has been properly configured.

7) Run each of the queries (2-3) one time each and the queries (4-5) two times each on your sharded system, and provide screenshots for the output of each run.

8) Design a suitable replication scheme to answer the above queries that uses the three machines gpel8.cs.ou.edu, gpel9.cs.ou.edu and gpel10.cs.ou.edu. You need to describe and justify your  replication design in detail. Then, implement your design in MongoDB. Your implementation must include the code to set up the replication scheme. For this task you only need to implement replication. You do not need to implement sharding for this task. You also need to provide a screenshot of the output of the command ‘db.printShardingStatus()’ when you run it in the shard controller so that we can verify that your sharding scheme was properly configured.

9) Run each of the queries (2-3) one time each and the queries (4-5) two times each on your replicated system. Provide screenshots for the output of each run.

10) In this task you will do a simple simulation of the failure of the primary node. To do this, perform the following sub-tasks:

        a. Connect to the machine running the primary of your replica set and stop the MongoDB process running on that machine. Do not attempt to shutdown or restart the machine.
    
        b. Immediately connect to another active MongoDB server in your replica set and run the command rs.status(). Take a screenshot that shows that no primary has yet been elected.
    
        c. Wait until a primary has been elected, and then run the queries (2-5) one time each again with the remaining nodes. Provide screenshots for the output of each run
