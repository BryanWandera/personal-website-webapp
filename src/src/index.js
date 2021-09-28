import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { PlaylistCard } from './components'

//do not forget to adjust the api domains

const userID = "nk0b80ekcsiwcpht16mym9gzr"

const fetchPlaylists = function (spotifyAccessToken, id) {
  //fetching the list of playlists from spotify but only after receiving the access token
  fetch(`https://api.spotify.com/v1/users/${userID}/playlists`, {
    method: "GET",
    headers: {
      'Authorization': `Bearer ${spotifyAccessToken}`,
      'Content-Type': 'application/json'


    }
  }).then((response) => {
    if (response.status === 200) {
      console.log("good")
      return response.json()
    } else if (response.status === 401) {
      spotifyAccessToken = getNewTokenThen()

      console.log("bad")
    }
  }).then(
    (data) => {
      let playlistsData = data.items
      console.log(playlistsData)

      const Playlists = function () {
        return (
          <div id= "playlists-grid">
            { playlistsData.map(playlist=>(
              <div>
                {PlaylistCard(playlist.images[0].url, playlist.name, playlist.description, playlist.id)}
              </div>
            )  ) }
          </div>
        )
        
      }

      ReactDOM.render(
        <Playlists></Playlists>,
        document.getElementById('root')
      );


    }

  ).catch((e) => {
    console.log(e)
  })
}

export const getNewTokenThen = function (callback, id) {
  //getting new token then passing it to a callback, so that fetchPlaylists can access the token

  
  fetch('http://127.0.0.1:8000/spotifyapi', {}).then(
    (response) => {
      if (response.status === 200) {
        let data = response.json()
        return data
      }

    }
  ).then((data) => {
    let access_token = data["access_token"]
    console.log(access_token)
    return access_token
  }).then((access_token) => {
    callback(access_token, id)
  }).catch(
    (e) => {
      console.log(e)

    }
  )
}

export const addPlaylistToLibrary = function(spotifyAccessToken, playlist_id){
  fetch(`https://api.spotify.com/v1/playlists/${playlist_id}/followers`, {
    method: 'PUT',
    headers : {
      'Authorization': `Bearer ${spotifyAccessToken}`
    }
  }).then((response)=>{
    if (response.status === 200){
      console.log("Success")
      alert('Added to library!😎')
    } else {
      console.log("Could not add playlist")
      alert('Oops, Maybe you already follow this playlist? 🙊 \nTry searching for it instead.')
    }
  }).catch((e)=>{
    console.log("Some shit went wrong")
    console.log(e)
  })
}

getNewTokenThen(fetchPlaylists)


