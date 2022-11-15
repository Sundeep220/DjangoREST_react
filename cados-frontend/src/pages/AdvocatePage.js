import React, {useEffect,useState}  from 'react'
import axios from 'axios'

import { useParams } from 'react-router-dom'
const AdvocatePage = () => {
    const params = useParams()
    const username = params.username
    const [advocate, setAdvocate] = useState(null)

    useEffect(() => {
        getData()
    },[username])

    let getData = async () => {
        let response = await axios.get(`http://127.0.0.1:8000/advocates/${username}`)
        console.log('Response', response)
        setAdvocate(response.data)
    }


  return (
    <>
        {advocate && (
            <div className= "advocate__preview_wrapper">
                <img className="advocate__preview__image" src={advocate.image}/>
            <strong>{advocate.username}</strong>
             <br/>
            <small><a href={advocate.twitter}>@{advocate.username}</a></small>
           
            <small><p className="advocate__preview__bio">{advocate.bio}</p></small>
        </div>


        )}     
            
    </>
    
  )
}

export default AdvocatePage