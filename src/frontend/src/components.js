import React from 'react';


export const PlaylistCard = function (imageURL, name, description, id){
    return (
        <div className={"playlist-container"}>
            <div className={"cover-image-container"} style={ {backgroundImage:`url(${imageURL})`}}></div>
            <p className={"playlist-name"}>{name}</p>
            <p className={"playlist-description"}>{description}</p>
            <button className={"follow-button"}>Add +</button>
        </div>
    )
}
