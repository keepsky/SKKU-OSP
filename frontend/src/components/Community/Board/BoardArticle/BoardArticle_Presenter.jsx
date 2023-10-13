import { useState } from 'react';
import '../Board.css';
import { BsHandThumbsUp, BsFillChatLeftTextFill, BsBookmark, BsEyeFill } from 'react-icons/bs';
import ProfileDropdown_Container from '../../ProfileDropdown';

export default function BoardArticle_Presenter(props) {
  const { article, pubDate, onArticle } = props;

  return (
    <div className="board-article">
      {article.title ? (
        <>
          <div>
            {article.writer ? (
              article.anonymous_writer ? (
                <span>익명</span>
              ) : (
                <ProfileDropdown_Container userName={article.writer.user.username} userId={article.writer.user.id} />
              )
            ) : (
              <span>탈퇴한 이용자</span>
            )}
            · {pubDate}
          </div>
          <h4 className="board-article-title" onClick={onArticle}>
            {article.title}
          </h4>
          <div>
            {article.tags.map((tag) => (
              <h6 className="inline board-article-tag" key={tag.name}>
                #{tag.name.replace(' ', '_')}&nbsp;
              </h6>
            ))}
            <div className="board-article-meta-list">
              <>
                <BsHandThumbsUp size={13} className="board-article-meta" /> {article.like_cnt}
              </>
              <>
                <BsFillChatLeftTextFill size={13} className="board-article-meta" /> {article.comment_cnt}
              </>
              <>
                <BsBookmark size={13} className="board-article-meta" /> {article.scrap_cnt}
              </>
              <>
                <BsEyeFill size={13} className="board-article-meta" /> {article.view_cnt}
              </>
            </div>
            <div className="float-clear"></div>
          </div>
        </>
      ) : (
        <h5>작성된 글이 없습니다.</h5>
      )}
    </div>
  );
}
