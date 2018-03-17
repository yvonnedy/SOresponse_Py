### Branch Coverage    
   
`web_page()`:      

| Condition | Test function |
| --- | -------- |
| the URL is not a valid SO webpage | `test_Url()` |  
| the URL is valid | `test_resultOfWebpage()` | 
     
`popular()`:   
    
| Condition | Test function |
| --- | -------- |
| the webpage has no response | `test_lenOfResponse()` |  
| the webpage has resonses; choice equals 'likes' | `test_resultOfLikes()` |  
| the webpage has resonses; choice equals 'author' | `test_resultOfAuthor()` |  
| the webpage has resonses; choice equals 'author'; no author accepted answer | `test_noAuthorAccepted()` | 
| the webpage has resonses; choice does not equal 'likes' or 'author | `test_inputOfChoice()` |        
    
`response_stat()`:    
    
| Condition | Test function |
| --- | -------- |
| webpage is loaded | `test_result()` |  


