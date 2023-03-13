import React from 'react'
import image1 from './img/image1.jpeg'
import styled from 'styled-components'

function Card() {
  return (
    <div className='card shadow-none p-3 mb-5 bg-light rounded bg-dark'>
        <img src={image1} alt="" />
        <div className='card-body bg-dark '>
            <h4 className='card-title text-light'  >Maxwell the Cat </h4>
            <p className='card-text text-secondaty text-light'>Lorem ipsum dolor, sit amet consectetur 
            adipisicing elit. Hic quas maiores asperiores accusantium perferendis,
            reiciendis, iste voluptatibus voluptatum consequuntur quo accusamus nulla
            quam tempore modi voluptatem nam, officia vitae sunt.</p>
            <Buttom>
            <button class="button"> Seguir
            </button>
            </Buttom>
            
        </div>
      Card
    </div>
  )
}

export default Card
const Buttom = styled.div`
.button {
    --color: #8f8ad2;
    padding: 0.8em 1.7em;
    background-color: transparent;
    border-radius: .3em;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: .5s;
    font-weight: 400;
    font-size: 17px;
    border: 1px solid;
    font-family: inherit;
    text-transform: uppercase;
    color: var(--color);
    z-index: 1;
   }
   
   .button::before, .button::after {
    content: '';
    display: block;
    width: 50px;
    height: 50px;
    transform: translate(-50%, -50%);
    position: absolute;
    border-radius: 50%;
    z-index: -1;
    background-color: var(--color);
    transition: 1s ease;
   }
   
   .button::before {
    top: -1em;
    left: -1em;
   }
   
   .button::after {
    left: calc(100% + 1em);
    top: calc(100% + 1em);
   }
   
   .button:hover::before, .button:hover::after {
    height: 410px;
    width: 410px;
   }
   
   .button:hover {
    color: rgb(10, 25, 30);
   }
   
   .button:active {
    filter: brightness(.8);
   }
   
   
`