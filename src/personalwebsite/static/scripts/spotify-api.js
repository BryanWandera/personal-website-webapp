const userID = "nk0b80ekcsiwcpht16mym9gzr"


const fetchPlaylists = function (spotifyAccessToken){    
    //fetching the list of playlists from spotify but only after receiving the access token
    fetch(`https://api.spotify.com/v1/users/${userID}/playlists`, {
        method: "GET",
        headers: {
            'Authorization': `Bearer ${spotifyAccessToken}`,
            
            
        }
    }).then((response)=>{
        if(response.status == 200){            
            console.log("good")
            return response.json()
        } else if (response.status == 401) {
            spotifyAccessToken=getNewTokenThen()
            
            console.log("bad")
        }
    }).then(
        (data)=>{    
            let playlistObjectsArray = data.items        
            console.log(playlistObjectsArray)
            return playlistObjectsArray
            
        }

    ).catch((e)=>{
        console.log(e)
    })
}

const getNewTokenThen = function (callback){
    //getting new token then passing it to a callback, so that fetchPlaylists can access the token
   fetch('http://127.0.0.1:8000/spotifyapi',{}).then(
       (response)=>{
          if (response.status == 200){
            let data = response.json()
            return data        
          } 
           
       }
   ).then((data)=>{
       let access_token = data["access_token"]
       console.log(access_token)
       return access_token
   }).then((access_token)=>{
       callback(access_token)
   }).catch(
       (e)=>{
           console.log(e)
           console.log("the math is not mathing")
       }
   )
}

getNewTokenThen(fetchPlaylists)
