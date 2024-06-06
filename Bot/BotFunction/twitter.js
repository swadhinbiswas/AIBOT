const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

app.post('/grab-twitter-links', async (req, res) => {
    const { twitterHandle } = req.body;
    
    if (!twitterHandle) {
        return res.status(400).json({ error: 'Twitter handle is required' });
    }
    
    try {
        const tweets = await getTweets(twitterHandle);
        const fileLinks = extractFileLinks(tweets);
        const fileName = 'twitter_file_links.json';
        
        fs.writeFileSync(fileName, JSON.stringify(fileLinks, null, 2));
        
        res.status(200).json({ message: 'File links extracted and saved', file: fileName });
    } catch (error) {
        res.status(500).json({ error: 'Error fetching tweets or processing data', details: error.message });
    }
});

// Function to get tweets (stub function, replace with actual implementation)
async function getTweets(handle) {
    // You will need to implement this function to fetch tweets using Twitter API
    // For now, return a mock array of tweets
    return [
        { text: 'Check this file out: https://example.com/file1.pdf' },
        { text: 'Another file link: https://example.com/file2.png' }
    ];
}

// Function to extract file links from tweets
function extractFileLinks(tweets) {
    const fileLinks = [];
    const fileLinkRegex = /(https:\/\/\S+\.(pdf|png|jpg|jpeg|docx|xlsx|txt))/g;
    
    tweets.forEach(tweet => {
        const matches = tweet.text.match(fileLinkRegex);
        if (matches) {
            fileLinks.push(...matches);
        }
    });
    
    return fileLinks;
}

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
