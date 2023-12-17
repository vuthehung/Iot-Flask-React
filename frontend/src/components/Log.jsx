import React from 'react';
import ReactPlayer from 'react-player';

const Log = () => {
  const videoName = '13-12-23-14-48-17.mp4'; // Tên video bạn muốn hiển thị

  const videoUrl = `http://127.0.0.1:5000/video/${videoName}`;
  return (
    <div>
        <div>
            <video width="100%" height="auto" controls>
                <source src={videoUrl} type="video/mp4" />
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
  );
};

export default Log;
