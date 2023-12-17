import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const Camera = () => {
    const [streamUrl, setStreamUrl] = useState("");
    const [isStreaming, setIsStreaming] = useState(true);

    const handleStartStream = () => {
    setStreamUrl('http://127.0.0.1:5000/stream');
    setIsStreaming(true);
    };

    const handleStopStream = () => {
    // Đặt URL của video thành một URL trống hoặc URL khác để dừng stream
    setStreamUrl('');
    setIsStreaming(false);
    };

    return (
        <Container>
            <Row>
                <Col>
                    <span>Camera trước cửa nhà</span>
                    <div>
                        <button onClick={handleStartStream}>Start Stream</button>
                        <button onClick={handleStopStream}>Stop Stream</button>
                        <div>
                            <img src={streamUrl} width='100%' height='100%'/>
                        </div>
                    
                    </div>
                </Col>
                <Col>
                    <span>Camera phòng khách</span>
                    <div>   
                        <button onClick={handleStartStream}>Start Stream</button>
                        <button onClick={handleStopStream}>Stop Stream</button>
                        <div>
                            <img src={streamUrl} width='100%' height='100%'/>
                        </div>
                    
                    </div>
                </Col>
            </Row>
        </Container>
    );
};

export default Camera;
