fn add_vectors(v1: &[f32], v2: &[f32]) -> Vec<f32> {
    v1.iter()
        .zip(v2.iter())
        .map(|(&x, &y)| x + y)
        .collect::<Vec<f32>>()
}
fn mul_vector_number(v1: &[f32], num: f32) -> Vec<f32> {
    v1.iter().map(|&i| i * num).collect::<Vec<f32>>()
}
