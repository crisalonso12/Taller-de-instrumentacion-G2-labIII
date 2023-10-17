const int s0Pin = 2;
const int s1Pin = 3;
const int s2Pin = 4;

const int s0Pin2 = 6;
const int s1Pin2 = 7;
const int s2Pin2 = 8;

void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  
  pinMode(s0Pin, OUTPUT);
  pinMode(s1Pin, OUTPUT);
  pinMode(s2Pin, OUTPUT);

  pinMode(s0Pin2, OUTPUT);
  pinMode(s1Pin2, OUTPUT);
  pinMode(s2Pin2, OUTPUT);
  Serial.begin(9600);
  
}


void loop() {
  char input;
  
  if (Serial.available() > 0) {
    input = Serial.read(); // Leer el valor ingresado como un número entero

    switch (input){
      case '1':
      digitalWrite(s0Pin, HIGH);
      digitalWrite(s1Pin, LOW);
      digitalWrite(s2Pin, LOW);
      Serial.println("ATE1");
      break;
      
      case '2':
      digitalWrite(s0Pin, LOW);
      digitalWrite(s1Pin, HIGH);
      digitalWrite(s2Pin, LOW);
      Serial.println("ATE2");
      break;
      
      case '3':
      digitalWrite(s0Pin, HIGH);
      digitalWrite(s1Pin, HIGH);
      digitalWrite(s2Pin, LOW);
      Serial.println("ATE3");
      break;
      
      case '4':
      digitalWrite(s0Pin, LOW);
      digitalWrite(s1Pin, LOW);
      digitalWrite(s2Pin, HIGH);
      Serial.println("SEG");
      break;
      
      case '5':
      digitalWrite(s0Pin, HIGH);
      digitalWrite(s1Pin, LOW);
      digitalWrite(s2Pin, HIGH);
      Serial.println("GAN1");
      break;
      
      case '6':
      digitalWrite(s0Pin, LOW);
      digitalWrite(s1Pin, HIGH);
      digitalWrite(s2Pin, HIGH);
      Serial.println("GAN2");
      break;
      
      case '7':
      digitalWrite(s0Pin, HIGH);
      digitalWrite(s1Pin, HIGH);
      digitalWrite(s2Pin, HIGH);
      Serial.println("GAN3");
      break;

      case 'a':
      digitalWrite(s0Pin2, HIGH);
      digitalWrite(s1Pin2, LOW);
      digitalWrite(s2Pin2, LOW);
      Serial.println("2ATE1");
      break;
      
      case 'b':
      digitalWrite(s0Pin2, LOW);
      digitalWrite(s1Pin2, HIGH);
      digitalWrite(s2Pin2, LOW);
      Serial.println("2ATE2");
      break;
      
      case 'c':
      digitalWrite(s0Pin2, HIGH);
      digitalWrite(s1Pin2, HIGH);
      digitalWrite(s2Pin2, LOW);
      Serial.println("2ATE3");
      break;
      
      case 'd':
      digitalWrite(s0Pin2, LOW);
      digitalWrite(s1Pin2, LOW);
      digitalWrite(s2Pin2, HIGH);
      Serial.println("2SEG");
      break;
            
      case 'e':
      digitalWrite(s0Pin2, HIGH);
      digitalWrite(s1Pin2, LOW);
      digitalWrite(s2Pin2, HIGH);
      Serial.println("2GAN1");
      break;
      
      case 'f':
      digitalWrite(s0Pin2, LOW);
      digitalWrite(s1Pin2, HIGH);
      digitalWrite(s2Pin2, HIGH);
      Serial.println("2GAN2");
      break;
           
      case 'g':
      digitalWrite(s0Pin2, HIGH);
      digitalWrite(s1Pin2, HIGH);
      digitalWrite(s2Pin2, HIGH);
      Serial.println("2GAN3");
      break;
    }
  }

  // Tiempo entre muestras en microsegundos (200 microsegundos para 2500 muestras por segundo)
  const unsigned long tiempo_entre_muestras = 200;

  //conversión a voltaje a una tasa de 2500 muestras por segundo para cada canal
  unsigned long tiempo_inicio = micros();
  while (micros() - tiempo_inicio < tiempo_entre_muestras) {
    
    // primer canal (A0)
    int valor_canal_0 = analogRead(A0);
    
    float voltaje_canal_0 = (valor_canal_0 / 1023.0) * 5.0;
    //voltaje_canal_0 = (voltaje_canal_0 - 2.5) * 1.0;
    
    // segundo canal (A1)
    int valor_canal_1 = analogRead(A1);
    
    float voltaje_canal_1 = (valor_canal_1 / 1023.0) * 5.0;
   // voltaje_canal_1 = 0;(voltaje_canal_1 - 2.5) * 1.0;
    
  
   Serial.print(voltaje_canal_0);
   Serial.print(",");
   Serial.println(voltaje_canal_1);
  }

  
  //delay(1);
  

}
