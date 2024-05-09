import React, { useEffect, useState } from "react";

import axios from "axios";

function App() {
  const [direction, setDirection] = useState("");

  // 키보드 입력 이벤트 핸들러
  const handleKeyDown = (event) => {
    switch (event.key) {
      case "ArrowLeft":
        sendDirection("1");
        break;
      case "ArrowRight":
        sendDirection("2");
        break;
      default:
        break;
    }
  };

  // 키보드 입력 이벤트 핸들러
  const handleKeyUp = (event) => {
    sendDirection("0");
  };

  // 방향 전송 함수
  const sendDirection = (direction) => {
    axios
      .get("http://127.0.0.1:5000/key?key=" + direction)
      .then(function (response) {
        setDirection(response.data);
        console.log(response.data);
      });
  };

  // 컴포넌트가 마운트될 때 키보드 이벤트 리스너 등록
  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    // 컴포넌트가 언마운트될 때 이벤트 리스너 해제
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, []); // 빈 배열을 전달하여 최초 렌더링 시에만 이펙트 실행

  return (
    <div className="App">
      <h1>WebSocket Communication with Keyboard Input</h1>
      <p>Use arrow keys to send direction to server:</p>
      <p>Current direction: {direction}</p>
    </div>
  );
}

export default App;
