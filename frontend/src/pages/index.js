import Head from "next/head";
import Image from "next/image";
import { Inter } from "next/font/google";
import styles from "@/styles/Home.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function Home({data, done}) {

  console.log('data : ', data)
  console.log('done : ', done)
 

  return (
    <div>
      <main>
      <h1>Available Campaigns</h1>
{/*  display data with a callback function */}
      {data.map((element)=> <div key={element.slug}>

        <div>
          <div>
            {/* <Image src={element.logo} height={120} width={120} alt="Campaign logo"/> */}
             <Image src={"/" + element.logo} alt="Campaign logo" height={120} width={120} /> 
          </div>
          <div>
            <h1>{element.title}</h1>
            <p>{element.description}</p>
            <p>{element.created_at}</p>
          </div>
        </div>
        
      </div>)}
      </main>
      
    </div>
  );
}

// fetch data

export async function getStaticProps() {
let data = []
  try {
    const response = await fetch("http://127.0.0.1:8000/api/campaigns/");
// la reponse doit etre transformé en json 
  data = await response.json();
    
  } catch (error) {
    
  }

  if (!data.length) {
    return {
      notFound: true,
    }
    
  }
  
// retourner le resultat comme un props toujours 
  return {
    props: {
      data: data,
      done: true,
    },
  };
}
