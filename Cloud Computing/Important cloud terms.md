# Important Cloud Terms
* **Region**: A geographic area (e.g., "East US" or "West Europe") where a cloud provider runs one or more data centers. You choose a region to keep resources close to users (lower latency), meet data-residency laws, and plan for disaster recovery.
* **Data Center**: A physical building full of servers, storage, and networking equipment, with its own power, cooling, and security. A region is made up of one or more data centers. Groups of separate data centers within a region are often called *availability zones*.
* **Service**: A specific capability the cloud provider offers that you can use on demand, such as virtual machines, databases, storage, or AI tools. You use the service without building or maintaining the underlying hardware yourself.
* **Subscription**: Your billing and access agreement with a cloud provider. It ties the resources you create to an account that gets charged, and it sets limits and permissions. Organizations often use several subscriptions to separate teams, projects, or environments (dev vs. production).
* **Resource**: A single instance of a service that you create and manage, such as one virtual machine, one storage account, or one database. Resources live inside a subscription (and on Azure, inside a *resource group*).
* **Agility**: How quickly you can get and change computing resources. In the cloud you can spin up servers in minutes instead of waiting weeks to buy and install hardware, so teams can experiment and ship faster.
* **Scalability**: The ability to increase capacity to handle more work.
  * *Vertical scaling (scale up)*: give a machine more power (more CPU or RAM).
  * *Horizontal scaling (scale out)*: add more machines.
* **Elasticity**: The ability to scale up **and down automatically** as demand changes, so you only pay for what you use. Example: a shopping site adds servers during a holiday sale and removes them afterward.
  * *Scalability vs. elasticity*: scalability is being *able* to grow; elasticity is growing and shrinking *automatically* to match demand in real time.

# Cloud Services
* **Infrastructure as a Service (IaaS)**: The provider gives you the raw building blocks (virtual machines, storage, networking). You manage the operating system, runtime, apps, and data. Most control, most responsibility.
  * Examples: Azure Virtual Machines, AWS EC2, Google Compute Engine.
  * Analogy: renting an empty apartment — you furnish and maintain it.
* **Platform as a Service (PaaS)**: The provider manages the infrastructure **and** the operating system/runtime. You just deploy your code and manage your app and data.
  * Examples: Azure App Service, AWS Elastic Beanstalk, Google App Engine, Heroku.
  * Analogy: renting a furnished apartment — you just bring your stuff.
* **Software as a Service (SaaS)**: A complete, ready-to-use application delivered over the internet. The provider manages everything; you just use it (usually through a browser).
  * Examples: Microsoft 365, Gmail, Salesforce, Dropbox.
  * Analogy: staying in a hotel — everything is handled for you.
* **Backend as a Service (BaaS)**: Ready-made backend features for web and mobile apps (user authentication, databases, file storage, push notifications) that you call through APIs/SDKs, so you can build the frontend without writing your own server code.
  * Examples: Firebase, Supabase, AWS Amplify.

## Shared Responsibility at a Glance
| Who manages it?       | On-Premises | IaaS     | PaaS     | SaaS     |
|-----------------------|-------------|----------|----------|----------|
| Applications & Data   | You         | You      | You      | Provider |
| Runtime & OS          | You         | You      | Provider | Provider |
| Servers & Storage     | You         | Provider | Provider | Provider |
| Networking & Facility | You         | Provider | Provider | Provider |

# Cloud Deployment Models
* **Public Cloud**: Computing resources owned and run by a third-party provider and shared by many customers (*multi-tenant*) over the internet. You pay only for what you use, and the provider handles all the hardware and maintenance.
  * Examples: Microsoft Azure, AWS, Google Cloud.
  * Pros: no upfront hardware cost, near-unlimited scalability, fast to get started.
  * Cons: less control over the underlying hardware and security, and it may not meet strict compliance needs.
  * Analogy: riding a public bus — you share it with others and pay per ride.
* **Private Cloud**: Cloud infrastructure used by **only one organization**. It can be hosted in the organization's own data center or by a third party, but the resources aren't shared with anyone else (*single-tenant*).
  * Examples: a company running VMware or OpenStack in its own data center, Azure Stack, AWS Outposts.
  * Pros: most control, customization, and security; easier to meet strict regulations (healthcare, finance, government).
  * Cons: expensive — you buy and maintain the hardware and need staff to run it; scaling is limited by what you own.
  * Analogy: owning your own car — full control, but you pay for and maintain it.
* **Hybrid Cloud**: A mix of public and private clouds (and often on-premises systems) connected so data and apps can move between them. Sensitive workloads can stay private while everything else uses the public cloud.
  * Example: keeping customer records in a private data center while running the public website in Azure, and "bursting" to the public cloud during traffic spikes.
  * Pros: flexibility to put each workload in the best place; helps with compliance and gradual cloud migration.
  * Cons: more complex to set up, secure, and manage across environments.
  * Analogy: owning a car but taking a rideshare when you need a bigger vehicle.

## Deployment Models at a Glance
|                    | Public Cloud      | Private Cloud           | Hybrid Cloud           |
|--------------------|-------------------|-------------------------|------------------------|
| Who uses it?       | Many customers    | One organization        | Both                   |
| Upfront cost       | Low               | High                    | Medium                 |
| Control & security | Less              | Most                    | Flexible               |
| Scalability        | Very high         | Limited by your hardware | High (burst to public) |
| Maintenance        | Provider          | You                     | Shared                 |