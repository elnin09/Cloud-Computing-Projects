package edu.illinois.storm;

import org.apache.storm.redis.common.mapper.RedisDataTypeDescription;
import org.apache.storm.redis.common.mapper.RedisStoreMapper;
import org.apache.storm.tuple.ITuple;

public class WordCountStoreMapper implements RedisStoreMapper {
  private final RedisDataTypeDescription description;
  private final String hashKey;

  public WordCountStoreMapper(final String hashKey) {
    this.hashKey = hashKey;
    description = new RedisDataTypeDescription(RedisDataTypeDescription.RedisDataType.HASH, hashKey);
  }

  @Override
  public RedisDataTypeDescription getDataTypeDescription() {
    return description;
  }

  @Override
  public String getKeyFromTuple(final ITuple tuple) {

    return "sample";
    //return tuple.getStringByField("word");
    // End
  }

  @Override
  public String getValueFromTuple(final ITuple tuple) 
  {
  return "sample"; 
    //return tuple.getStringByField("count");
		// End
  }
}
