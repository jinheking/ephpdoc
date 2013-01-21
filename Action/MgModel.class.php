<?php
/**
 * @author eagle
 * @version Version 0.01.4
 * <span>创建日期:2011-05-13 星期五 黑色星期五</span>
 *
 * 在我们做了find()操作，获得$cursor游标之后，这个游标还是动态的，也就是在我获得游标到我循环操作完成对应记录的过程中，默认情况下，这对符合条件的记录如果增加，结果集也会自动增加。换句话说，在我find()之后，到我的游标循环完成这段时间，如果再有符合条件的记录被插入到collection,那么这些记录也会被$cursor获得。<br/>
 * 如果你想在获得$cursor之后的结果集不变化，需要这样做：<br/>
 * $cursor = $coll->find($query,$fields);<br/>
 * $cursor->snapshot();<br/>
 * 2011-6-13 添加limit功能这个便于分页使用<br/>
 * 2011-6-15添加distinct功能
 *
 */
class MgModel{
	
    // 模型名称
    protected $name = '';
    
    public function __construct($name=''){
    	if(!empty($name)) {
            $this->name = $name;
        }elseif(empty($this->name)){
            $this->name = substr(get_class($this),0,-5);
        }
		if($this->name!='Mg'){
			$this->db_config = array (
	          'username'  =>   	C('MG_USER'),
	          'password'   =>   C('MG_PWD'),
	          'hostname'  =>  	C('MG_HOST'),
	          'hostport'    =>  C('MG_PORT'),
	          'database'   =>   C('MG_NAME'),
			);
			$this->database='';
			$this->recordset='';
			$this->connect();
			$this->collection($this->name);
		}
    }
    
	/**
	 * mongo数据库的连接
	 * @return database database 返回连接数据库的指针
	 */
	public function connect() {
		$strconnect='mongodb://';
		$strconnect.=$this->db_config['username'];
		$strconnect.=':';
		$strconnect.=$this->db_config['password'];
		$strconnect.='@';
		$strconnect.=$this->db_config['hostname'];
		$strconnect.=':';
		$strconnect.=$this->db_config['hostport'];
		$strconnect.='/';
		$strconnect.=$this->db_config['database'];
		
		$this->db = new Mongo($strconnect);
			
		//dump($this->db);
		$this->database=$this->connectdb($this->db_config['database']);
		return $this->database;
	}

	/**
	 * 连接recordset
	 * @param strcollect string recordset名字
	 * @return $this->recordset recordset 返回recordset指针
	 */
	public function collection($strcollect){
		$this->recordset=$this->database->selectCollection($strcollect);
		return $this->recordset;
	}

	/**
	 * 连接database
	 * @param $strdb string 连接database的名字
	 * @return database database 返回连接数据库的指针
	 */
	private function connectdb($strdb) {
		$this->database=$this->db->selectDB($strdb);
		return $this->database;
	}
	/**
	 * 插入数据
	 * @param $arr array  保存数据
	 * @return 无
	 */
	function save($arr){
		$this->recordset->insert($arr);
	}
	/**
	 * 批量插入数据
	 * @param $arr array  保存数据
	 * @return result bool 是否插入成功
	 * insert的第二个参数array $options 选项
	 * safe 是否返回操作结果信息
	 */
	public function batchInsert($arr){
		return $this->recordset->batchInsert($arr,array('safe'=>true));
	}
	/**
	 * 插入数据
	 * @param $arr array  保存数据
	 * @return result bool 是否插入成功
	 * insert的第二个参数array $options 选项
	 * safe 是否返回操作结果信息
	 * fsync 是否直接插入到物理硬盘
	 */
	public function insert($arr){
		
		return $this->recordset->insert($arr,array("safe"=>true));
	}
	/**
	 * 删除数据
	 * @param $arr array  删除数据
	 * @return 返回是否删除成功
	 */
	public function delete($arr,$option){
		
		if(empty($option)){
			$option=false;
		}
		return $this->recordset->remove($arr,array("safe"=> $option));
	}
	/**
	 * 修改数据,只修改符合条件的第一条
	 * @param $arr array  修改条件
	 * @param $newdata array  要修改成的数据
	 * @param $option boolean  修改的方式false只修改一条，true全部修改满足条件的
	 * 修改方式有
	 * 1)"upsert" if no document matches $criteria, a new document will be created from $criteria and $newobj (see upsert example below).
	 * 2)"multiple" 修改数量，默认的是false,也就只修改一条
	 * 例子
	 * 1）update(array("uid"=>'1'), array('$set' => array("uid" => 1))
	 * 2）update(array("uid"=>'1'), array('$inc' => array("count" => 1))
	 *
	 * @return 无
	 */
	public function update($arr,$newdata,$option){
		
		if(empty($option)){
			$option=false;
		}
		return $this->recordset->update($arr,$newdata,array("multiple" => $option,"safe"=>true));
	}
	/**
	 * 
	 * 修改数据，采用自加的方式
	 * @param $arr array  修改条件
	 * @param $inc array 自加多少
	 */
	public function inc($arr,$inc){
		
		return $this->recordset->update($arr,array('$inc' => $inc), array("upsert" => true));
		
	}
	
	/**
	 *
	 * @param skip integer 掠过的数据
	 * @param limit integer 选取的数量
	 * @param arr array 查询的数组
	 * @param sort array 排序的数组 1表示升序(asc)，-1表示降序(desc)
	 * @return list array 结果数组
	 *
	 */
	public function limit($skip,$limit,$sort,$querryarr){
		if(empty($querryarr)){
			$querryarr=array();
		}
		if(empty($sort)){
			$sort=array();
		}
		return $this->recordset->find($querryarr)->sort($sort)->skip($skip)->limit($limit);
			
	}
	/**
	 * 查询数据
	 * @param arr array 查询的数组
	 * @param sort array 排序的数组 1表示升序(asc)，-1表示降序(desc)
	 * @return list array 结果数组游标
	 */
	public function query($arr,$sort){
		if(empty($arr)){
			$arr=array();
		}
		if(!empty($sort)){
			return $this->recordset->find($arr)->sort($sort);
		}else{
			return $this->recordset->find($arr);
		}
	}
	
	/**
	 * 查询数据
	 * @param arr array 查询的数组
	 * @param sort array 排序的数组 1表示升序(asc)，-1表示降序(desc)
	 * @return list array 结果数组
	 */
	public function select($arr,$sort){
		if(empty($arr)){
			$arr=array();
		}
		if(!empty($sort)){
			$cursor=$this->recordset->find($arr)->sort($sort);
		}else{
			$cursor= $this->recordset->find($arr);
		}
		$result=array();
		foreach($cursor as $c){
			$result[]=$c;
		}
		return $result;
	}

	/**
	 * like查询数据
	 * @param  arr array 查询的数组
	 * @return list array 结果数组
	 *
	 *  使用方法：
	 *  array_push($arr,array('title','blog','right'));
	 *  array_push($arr,array('uid','10','left'));
	 *  array_push($arr,array('url','12','all'));
	 *  $cursor=$mg->likeQuery($arr);
	 *  只有这三种简单的查询，其他的复杂的比如not什么的，目前需要自己写正则表达式
	 */
	public function likeQuery($arr){
		$arrQuery=array();
		if(empty($arr)){
			$arr=array();
		}else{
			foreach ($arr as $a){
				switch ($a[2]) {
					case "all":
						array_push($arrQuery,array($a[0] => new MongoRegex('/'.$a[1].'/i')));
						break;
					case "left":
						array_push($arrQuery,array($a[0] => new MongoRegex('/^'.$a[1].'/i')));
						break;
					case "right":
						array_push($arrQuery,array($a[0] => new MongoRegex('/'.$a[1].'$/i')));
						break;
				}

			}
		}
		return $this->recordset->find($arrQuery);
	}
	
	/**
	 * 对collection进行distinct
	 * @param $distinct_key string 限制条件，目前只能够单列进行distinct
	 * @return list array 结果数组
	 */
	public function distinct($distinct_key){
		return $this->database->command(array("distinct" => $this->recordset->getName(), "key" => $distinct_key));
		
	}
	
	/**
	 * 
	 */
	 private function ggg(){
	 	
	 }
}