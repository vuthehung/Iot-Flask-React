import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const Camera = () => {
    const [streamUrl1, setStreamUrl1] = useState("");
    const [streamUrl2, setStreamUrl2] = useState("");
    const [isStreaming1, setIsStreaming1] = useState(true);
    const [isStreaming2, setIsStreaming2] = useState(true);

    const handleStartStream = () => {
    setStreamUrl1('http://127.0.0.1:5000/stream');
    setIsStreaming1(true);
    };

    const handleStopStream = () => {
    // Đặt URL của video thành một URL trống hoặc URL khác để dừng stream
    setStreamUrl1('');
    setIsStreaming1(false);
    };
    
    const handleStartStream2 = () => {
        setStreamUrl2('http://127.0.0.1:5000/stream2');
        setIsStreaming2(true);
        };
    
    const handleStopStream2 = () => {
        // Đặt URL của video thành một URL trống hoặc URL khác để dừng stream
        setStreamUrl2('');
        setIsStreaming2(false);
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
                            <img src={streamUrl1} width='100%' height='100%' alt='Camera đã tắt'/>
                        </div>
                    
                    </div>
                </Col>
                <Col>
                    <span>Camera phòng khách</span>
                    <div>   
                        <button onClick={handleStartStream2}>Start Stream</button>
                        <button onClick={handleStopStream2}>Stop Stream</button>
                        <div>
                            <img src={streamUrl2} width='100%' height='100%' alt='Camera đã tắt'/>
                        </div>
                    
                    </div>
                </Col>
            </Row>
        </Container>
    );
};

export default Camera;
