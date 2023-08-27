import '../Community.css';
import CommunityNavItem from './CommunityNavItem/index';
import BoardArticle from './BoardArticle/index';
import LoaderIcon from 'react-loader-icon';

export default function Board_Presenter(props) {
  const { isLoadedArticles, articles, onWrite, tabName } = props;

  return (
    <div className="col-9">
      <div className="community-nav d-flex">
        <button className="hidden">hidden</button>
        <ul className="nav nav-fill community-nav-items">
          <CommunityNavItem navName="자유" tabName={tabName} />
          <CommunityNavItem navName="질문" tabName={tabName} />
          <CommunityNavItem navName="정보" tabName={tabName} />
          <CommunityNavItem navName="홍보" tabName={tabName} />
        </ul>
        <button type="button" className="btn btn-primary" onClick={onWrite}>
          작성하기
        </button>
      </div>

      {isLoadedArticles ? (
        <>
          {articles.length ? (
            articles.map((article) => <BoardArticle key={article.id} article={article} />)
          ) : (
            <BoardArticle article={{}} />
          )}
        </>
      ) : (
        <LoaderIcon style={{ marginTop: '20px' }} />
      )}
    </div>
  );
}
