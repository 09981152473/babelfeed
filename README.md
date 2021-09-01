## Babel Feed: A Podcast hosting Platform

Website: www.babelfeed.com/

Test Account

User Name:  testuser

Password:   testpassword1

### Overview
This project allows users to create and manage podcast shows and episodes. When a user creates a show, they are provided
with a form that asks for all the necessary information to form a podcasts that will be considered valid 
for different podcast feeds. Users can upload image files for show and episode thumbnails and audio files to create
new episodes. These files are stored in an AWS S3 bucket. Files are automatically deleted if a user decides
to delete a show or change the thumbnail of a show or the audio of an episode.

The real benefit of this platform is the ability to dynamically generate an RSS feed for your show that can be added to
podcast indexers and listening apps. The feed is generated in accordance to iTunes recommended standards and has a few other
tags that other podcast indexers require.

Download through for the shows and visits through social media associated for the shows are routed through the backend,
allowing for the collection of download metrics. Each user has a metrics dashboard where they can find statistics about 
download count, audience traffic, and peak download times.

I've also written many test cases for models and forms to catch issues early and implemented some basic security measures 
around user uploads.


TODO:
* Refactor models to be 'fatter' and views to be 'thinner'
* Test cases for views and urls
* Stripe Integration
* Research best practices for security
  * AWS policies
  * Django security practices
  * Heroku hosting security practices
* Clean up some inconsistent naming patterns
* Condense some of the apps? (does content and metrics_dashboard need to be separate?)

### Apps
#### Accounts
This app contains the logic around logging in, registering users, and automatically generating a profile model. 

### Content
This app handles pulling the content from the aws 

#### Manage
This app is where the logic and models for shows and episodes are kept. 

### Metrics Dashboard
This app displays the metrics for a user's shows and episodes.

### Shows Frontend
This app displays the frontend for a particular show, including all the episodes and webplayer.


#### Manual
This is a placeholder for now. Users can use a side menu navigate a manual that will provide info about how to
use the platform.

#### Articles
This is a placeholder for now. Users will be able to read articles about podcasting, including news and tips to 
grow their shows.

### Payment
This is a placeholder for stripe integration so that we can monitize this platform.
