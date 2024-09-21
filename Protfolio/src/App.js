import profile from './프로필사진.png';
import { useEffect } from 'react';
import './App.css';

function App() {
  useEffect(() => {
    const container = document.querySelector('.container'); // 요소 선택

    const handleMouseMove = (e) => {
      const x = e.offsetX;
      const y = e.offsetY;

      const rotateY = (-1 / 5) * x + 20; // Y축 회전 각도 계산
      const rotateX = (2 / 15) * y - 20; // X축 회전 각도 계산

      container.style.transform = `perspective(700px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    };

    const handleMouseLeave = () => {
      container.style.transition = 'transform 0.3s'; // 부드러운 전환 효과
      container.style.transform = `perspective(700px) rotateX(0deg) rotateY(0deg)`;
    };

    if (container) {
      container.addEventListener('mousemove', handleMouseMove);
      container.addEventListener('mouseleave', handleMouseLeave); // 마우스 아웃 이벤트 추가
    }

    return () => {
      if (container) {
        container.removeEventListener('mousemove', handleMouseMove);
        container.removeEventListener('mouseleave', handleMouseLeave); // 언마운트 시 제거
      }
    };
  }, []);
  

  return (
    <div className="App">
      <header className='heading'>
        <div className='headingText'>메인</div>
      </header>
      <main className='mainPage'>
        <div className='UX_profile'>
          <div className='mainAndSubTitle'>
            <div className='mainTitle'> UX / UI DESIGNER</div>
            <div className='mainTitle'> & FRONT-END</div>
            <div className='subTitle'>저만의 스타일과 유행의 조화를 이루는 조하민입니다.</div>
          </div>
          <div className='overlay'></div>
          <div className='container'>
            <img src={profile} className='imgTitle' alt='프로필 사진' />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
