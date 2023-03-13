import React from 'react';
import './ClienteLayout.scss';

export function ClienteLayout(props) {
  const { children } = props;  
  return (
    <div>
      <p> Cliente Layout</p>
      {children}
    </div>
  );
}


