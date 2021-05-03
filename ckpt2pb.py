import tensorflow as tf

meta_path = 'icdar/4/model.ckpt-11111.meta' # Your .meta file
output_node_names = ['feature_fusion/Conv_7/Sigmoid', 'feature_fusion/concat_3']    # Output nodes

with tf.Session() as sess:
    # Restore the graph
    saver = tf.train.import_meta_graph(meta_path)

    # Load weights
    saver.restore(sess,tf.train.latest_checkpoint('icdar/4/model.ckpt-11111'))

    # Freeze the graph
    frozen_graph_def = tf.graph_util.convert_variables_to_constants(
        sess,
        sess.graph_def,
        output_node_names)

    # Save the frozen graph
    with open('output_graph.pb', 'wb') as f:
      f.write(frozen_graph_def.SerializeToString())

# Below is working
# import os
# import tensorflow as tf

# trained_checkpoint_prefix = 'icdar/4/model.ckpt-11111'
# export_dir = os.path.join('export_dir', '1')

# graph = tf.get_default_graph()#tf.Graph()
# with tf.Session(graph=graph, config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
#     # Restore from checkpoint
#     loader = tf.train.import_meta_graph('icdar/4/model.ckpt-11111.meta')
#     loader.restore(sess, trained_checkpoint_prefix)

#     # Export checkpoint to SavedModel
#     builder = tf.saved_model.builder.SavedModelBuilder(export_dir)
#     builder.add_meta_graph_and_variables(sess,
#                                          [tf.saved_model.tag_constants.TRAINING, tf.saved_model.tag_constants.SERVING],
#                                          strip_default_attrs=True)
#     builder.save()   