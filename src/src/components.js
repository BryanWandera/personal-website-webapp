import React from 'react';
import { addPlaylistToLibrary, getNewTokenThen } from './index.js';

export const PlaylistCard = function (imageURL, name, description, id) {
    return (
        <div key={id} className={"playlist-container"}>
            <div className={"cover-image-container"} style={{ backgroundImage: `url(${imageURL})` }}></div>
            <p className={"playlist-name"}>{name}</p>
            <p className={"playlist-description"}>{description}</p>
            <button onClick={ function(){getNewTokenThen(addPlaylistToLibrary, id)} } className={"follow-button"}>Add +</button>
        </div>
    )
}
