import React, { useState, useEffect } from 'react';
import { Container, Col, Row } from 'react-bootstrap';
import BootstrapSwitchButton from 'bootstrap-switch-button-react';

const API_BASE = "http://127.0.0.1:5000";

const Control = () => {
    const [camera1, setCamera1] = useState(false);
    const [camera2, setCamera2] = useState(false);

    useEffect(() => {
        fetch(API_BASE + "/get-armed")
          .then((res) => res.json())
          .then((data) => {
            setCamera1(data["armed"]);
          })
          .catch(() => alert("Không tìm thấy camera."));
      }, []);    

    const handleCamera1Toggle = () => {
        const options = {
            method: "POST",
        };
        setCamera1(!camera1);
        if(camera1) fetch(API_BASE + "/disarm", options)
        else fetch(API_BASE + "/arm", options)
    };

    const handleCamera2Toggle = () => {
    // Call your API to toggle Camera 2
    setCamera2(!camera2);
    };

  return (
        <Container className="justify-content-center align-items-center vh-100">
            <Row>
                <Col >
                    <span>Camera trước cửa nhà</span>
                    <div>
                        <BootstrapSwitchButton
                            checked={camera1}
                            onlabel="Bật"
                            offlabel="Tắt"
                            onChange={handleCamera1Toggle}
                            width={150}
                        />
                    </div>
                </Col>

                <Col>
                    <span>Camera phòng khách</span>
                    <div>
                        <BootstrapSwitchButton
                            checked={camera2}
                            onlabel="Bật"
                            offlabel="Tắt"
                            onChange={handleCamera2Toggle}
                            width={150}
                        />
                    </div>
                </Col>
            </Row>
        </Container>
  );
};

export default Control;