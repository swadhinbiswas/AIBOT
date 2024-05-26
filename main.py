
from logging import DEBUG, getLogger, StreamHandler, Formatter, FileHandler,WARNING,ERROR,CRITICAL,INFO,basicConfig
from Bot.bot import Bot


basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
              
              level=INFO)
  
  

logger = getLogger(__name__)




app=Bot.app
      
app.run()