import '../Board.css';
import { BsHandThumbsUp, BsFillChatLeftTextFill, BsBookmark, BsEyeFill } from 'react-icons/bs'

export default function BoardArticle_Presenter(props) {
  const { article, onArticle, onWriter } = props;

  return <div className="board-article">
    <h6>{ article.writer ? (
    article.anonymous_writer ?
    <span>익명</span> :
    <span className='board-article-writer' onClick={onWriter}>{article.writer.user.username}</span>
    ) : (
      <span>탈퇴한 이용자</span>
    )} · {article.pub_date.substring(0, 10)}</h6>
    <h4 className='board-article-title' onClick={onArticle}>{article.title}</h4>
    <div>
      <h6 className='inline'>#hashtag</h6>
      <div className='board-article-meta-list'>
        <><BsHandThumbsUp size={13} className='board-article-meta' /> {article.like_cnt}</>
        {/* <><BsFillChatLeftTextFill size={13} className='board-article-meta' /> {article.comment_cnt}</> */}
        <><BsBookmark size={13} className='board-article-meta' /> {article.scrap_cnt}</>
        <><BsEyeFill size={13} className='board-article-meta' /> {article.view_cnt}</>
      </div>
    </div>
  </div>;
}
