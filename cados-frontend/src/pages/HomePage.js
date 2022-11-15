import React, { useEffect, useState }  from 'react'
import axios from 'axios'
import {Link} from 'react-router-dom'
const HomePage = () => {
    const [advocates, setAdvocates] = useState([])
    const [total, setTotal] = useState(0)
    const [pagination, setPagination] = useState(null)

    useEffect(() => {
        getData()
    },[])

    let getData = async (query = '') => {
        // let response = await axios.get(`https://cados.up.railway.app/advocates/?query=${query}`)
        let response = await axios.get(`http://127.0.0.1:8000/advocates/?query=${query}`)
        console.log('Response', response)
        setAdvocates(response.data)
        // setTotal(response.data.total)
        // setPagination(response.data.pagination)
    }

    let searchData = (e) =>{
        e.preventDefault()
        let query = e.target.query.value
        getData(query)
    }
  return (
    <div className="main--container">
        <h1>Search engine for twitter users using TwitterAPI.</h1>
        <p>{pagination?.results_found} Developer advocates found</p>
        <div className="form--wrapper">
            <form  onSubmit={searchData} id="search__form">
                <input type="text" name="query" placeholder="Search here..."></input>
                <input className = "btn-primary" type="submit" value="search"/>
            </form>
        </div>
        <div className="advocate__list">
            {advocates.map((advocate, index) => (
                <div className= "advocate__preview_wrapper" key={index}>

                    <div className="advocate__preview__header">
                        <Link to={`/advocate/${advocate.username}`}>
                            <img className="advocate__preview__image" src={advocate.image}/>
                        </Link>
                        <div>
                            <strong>{advocate.name}</strong>
                            <br/>
                            <small><a href={advocate.twitter}>@{advocate.username}</a></small>
                        </div>
                    </div>
                    <small className="advocate__preview__bio"><p>{advocate.bio}</p></small>
                </div>
           ))}
        </div>
    </div>
  )
}

export default HomePage